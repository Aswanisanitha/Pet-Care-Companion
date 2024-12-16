from django.shortcuts import render, redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from supabase import create_client
import uuid
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
import os
import numpy as np
from PIL import Image
from skimage.io import imread
from keras.models import load_model
from django.http import JsonResponse
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Create your views here.



supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
MODEL_PATH = os.path.join( "catdog.h5")
model = load_model(MODEL_PATH)


def predict_image(request):
    # Default value for predicted_class to avoid uninitialized variable errors
    predicted_class = "No prediction made"

    if request.method == "POST" and request.FILES.get("image"):
        uploaded_image = request.FILES["image"]

        # Save uploaded image temporarily
        temp_image_path = "Assets/Detection/Input/temp_image.jpg"
        with open(temp_image_path, "wb") as f:
            for chunk in uploaded_image.chunks():
                f.write(chunk)

        try:
            # Preprocess the image
            img = image.load_img(temp_image_path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            # Make prediction
            preds = model.predict(x)
            out = decode_predictions(preds, top=1)
            predicted_class = out[0][0][1]  # Get the predicted class

            # Replace underscores with spaces for better readability
            predicted_class = predicted_class.replace("_", " ").title()

        except Exception as e:
            predicted_class = f"Error during prediction: {str(e)}"

        finally:
            # Clean up the temporary file
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)

        return render(request, "User/BreedFind.html", {"prediction": predicted_class})
    else:
        return render(request, "User/BreedFind.html")

def send_vaccine_reminders():
    tomorrow = now().date() + timedelta(days=1)
    print(tomorrow)
    reminders = tbl_vaccinedetails.objects.filter(vaccine_fordate=tomorrow)
    
    for reminder in reminders:
        subject = "Vaccine Reminder"
        body = f"""
        Dear User,

        This is a reminder about your pet's vaccination:
        Vaccine Name: {reminder.vaccine_name}
        Vaccine Details: {reminder.vaccine_details}
        Scheduled Date: {reminder.vaccine_fordate}

        Please make sure your pet gets the vaccine on time.

        Regards,
        Pet Care Companion Team
        """
        recipient_email = reminder.pet_id.user.user_email  
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [recipient_email],
        )

def homepage(request):
    return render(request,'User/Homepage.html')

def myprofile(request):
    user=tbl_userreg.objects.get(user_id=request.session["uid"])
    return render(request,'User/Myprofile.html',{"user":user})


def editprofile(request):
    user=tbl_userreg.objects.get(user_id=request.session["uid"])
    if request.method=="POST":
        user.user_name=request.POST.get('name')
        user.user_email=request.POST.get('email')
        user.user_contact=request.POST.get('Contact')
        user.user_address=request.POST.get('address')
        user.save()
        return redirect('User:myprofile')
    else:
         return render(request,'User/Editprofile.html',{"user":user})


def changepassword(request):
    user=tbl_userreg.objects.get(user_id=request.session["uid"])
    if request.method=="POST":
        pswd=user.user_password
        oldpswd=request.POST.get('oldpswd')
        newpswd=request.POST.get('newpswd')
        repswd=request.POST.get('repswd')
        if pswd==oldpswd:
            if newpswd == repswd:
                user.user_password=newpswd
                user.save()
                return redirect('User:myprofile')
            else:
                return render(request,'User/changepassword.html',{'error':"Different Password"})
        else:
            return render(request,'User/changepassword.html',{'error':"Invalid Password"})
    else:
        return render(request,'User/Changepassword.html')



def pet(request):
    user=tbl_userreg.objects.get(user_id=request.session['uid'])
    pettype=tbl_pettype.objects.all()
    pet=tbl_pet.objects.filter(user_id=user)
   
    if request.method=="POST":
        name=request.POST.get("name")
        weight=request.POST.get("weight")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        photo=request.FILES.get("photo")


        if photo:
            try:
            
                file_name = f"PetDocs/{photo.name}"
                photo_content = photo.read()
                storage_response = supabase.storage.from_("petcare").upload(file_name, photo_content)
                photo_url = supabase.storage.from_("petcare").get_public_url(file_name)
            except Exception as e:
                print(e)
                return render(request, "User/Pet.html", { "msg": "Failed to upload photo."})
        else:
            photo_url = None  # Handle cases where no photo is uploaded
        tbl_pet.objects.create(
            breed=tbl_breed.objects.get(id=request.POST.get('breed')),
            pet_name=name,pet_photo=photo_url,pet_weight=weight,pet_age=age,pet_gender=gender,user_id=user
        )
        return render(request,'User/Pet.html',{'msg':"Data inserted"})
    else:
      
        return render(request,'User/Pet.html',{'pet':pet,'type':pettype})



def ajaxbreed(request):
    type_id= request.GET.get('did')
    breed = tbl_breed.objects.filter(pettype=type_id)
    return render(request, "User/Ajaxbreed.html", {'breed': breed})

def delpet(request,id):
    tbl_pet.objects.get(id=id).delete()
    return redirect("User:pet")


def gallery(request,id):
    gallery=tbl_gallery.objects.filter(pet_id=id)
    if request.method=="POST":
        title=request.POST.get('title')
        photo=request.FILES.get("file")

        if photo:
            try:
            
                file_name = f"Petgallery/{photo.name}"
                photo_content = photo.read()
                storage_response = supabase.storage.from_("petcare").upload(file_name, photo_content)
                photo_url = supabase.storage.from_("petcare").get_public_url(file_name)
            except Exception as e:
                print(e)
                return render(request, "User/Gallery.html", { "msg": "Failed to upload photo."})
        else:
            photo_url = None  

        tbl_gallery.objects.create(
            gallery_file=photo_url,gallery_title=title,pet_id=tbl_pet.objects.get(id=id)
        )
        
        return render(request,'User/Gallery.html',{'msg':"Data inserted"})
    else:
      
        return render(request,'User/Gallery.html',{'gallery':gallery})



def delgallery(request,id):
    tbl_gallery.objects.get(id=id).delete()
    return redirect("User:gallery")


def viewpets(request):
    pet=tbl_pet.objects.all()
    return render(request,'User/Viewpets.html',{"view":pet})

def viewgallery(request,id):
    file=tbl_gallery.objects.filter(pet_id=id)
    return render(request,'User/Viewgallery.html',{"view":file})



def complaint(request):
    user=tbl_userreg.objects.get(user_id=request.session['uid'])
    complaint=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        tbl_complaint.objects.create(
            complaint_title=title, complaint_content=content , user_id=user
        )
        return render(request,'User/Complaint.html',{'msg':"Data inserted"})
    else:
        return render(request,'User/Complaint.html',{'complaint':complaint})


def delcomplaint(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("User:complaint")


def feedback(request):
    user=tbl_userreg.objects.get(user_id=request.session['uid'])
    feedback=tbl_feedback.objects.all()
    if request.method=="POST":
        content=request.POST.get("content")
        tbl_feedback.objects.create(
            feedback_content=content ,user_id=user
        )
        return render(request,'User/Feedback.html',{'msg':"Data inserted"})
    else:
        return render(request,'User/Feedback.html',{'feedback':feedback})


def delfeedback(request,id):
    tbl_feedback.objects.get(id=id).delete()
    return redirect("User:feedback")


def training(request):
    pettype=tbl_pettype.objects.all()
    training=tbl_traning.objects.all()
    return render(request,'User/Training.html',{'pettype':pettype,'training':training})

def ajaxtraining(request):
    pettype=request.GET.get("pid")
    breed=request.GET.get("did")
    training=tbl_traning.objects.filter(breed=breed,breed__pettype__id=pettype)
    return render(request,'User/AjaxTraining.html',{'training':training})

def food(request):
    pettype=tbl_pettype.objects.all()
    food=tbl_food.objects.all()
    foodplan=tbl_foodplan.objects.all()
    return render(request,'User/Food.html',{'pettype':pettype,'food':food,'foodplan':foodplan})

def ajaxfood(request):
    pettype=request.GET.get("pid")
    breed=request.GET.get("did")
    food=tbl_foodplan.objects.filter(breed=breed)
    return render(request,'User/Ajaxfood.html',{'food':food})

def activity(request):
    pettype=tbl_pettype.objects.all()
    activity=tbl_activity.objects.all()
    return render(request,'User/Activity.html',{'pettype':pettype,'activity':activity})

def ajaxactivity(request):
    pettype=request.GET.get("pid")
    breed=request.GET.get("did")
    activity=tbl_activity.objects.filter(breed=breed,breed__pettype__id=pettype)
    return render(request,'User/Ajaxactivity.html',{'activity':activity})


def abnormalactivity(request):
    pettype=tbl_pettype.objects.all()
    abactivity=tbl_abnormalactivity.objects.all()
    return render(request,'User/Abnormalactivity.html',{'pettype':pettype,'abactivity':abactivity})

def ajaxabactivity(request):
    pettype=request.GET.get("pid")
    breed=request.GET.get("did")
    abactivity=tbl_abnormalactivity.objects.filter(breed=breed,breed__pettype__id=pettype)
    return render(request,'User/Ajaxabnormalactivity.html',{'abactivity':abactivity})

    
def vetinaryhospital(request):
    district=tbl_district.objects.all()
    vhospl=tbl_vetinaryhospital.objects.all()
    return render(request,'User/Vetinaryhospital.html',{'district':district,'vhospl':vhospl})


def ajaxhospital(request):
    place = request.GET.get('did')
    vhospl= tbl_vetinaryhospital.objects.filter(place_id=place)
    return render(request, "User/AjaxHospital.html", {'vhospl': vhospl})
    

def slot(request, id):
    slot = tbl_slot.objects.filter(vetinaryhospital_id=id)
    user = tbl_userreg.objects.get(user_id=request.session["uid"])
    
    if request.method == "POST":
        fordate = request.POST.get("date")
        slot_id = tbl_slot.objects.get(id=request.POST.get("slot"))
        
        
        appointment_count = tbl_appoinment.objects.filter(slot=slot_id, appoinment_Fordate=fordate).count()
        
        if appointment_count >= int(slot_id.slot_count):
            return render(request, 'User/Slot.html', { 'slot': slot, 'error': "The selected slot is full. Please choose another slot."})
        else:
          
            token_number = appointment_count + 1
            
            
            tbl_appoinment.objects.create(
                slot=slot_id,
                user_id=user,
                appoinment_Fordate=fordate,
                appoinment_token=token_number  
            )
            return redirect("User:myappoinment")
    else:
        return render(request, 'User/Slot.html', {'slot': slot})




def myappoinment(request):
    user=tbl_userreg.objects.get(user_id=request.session['uid'])
    appoinment=tbl_appoinment.objects.filter(user_id=user)
    return render(request,'User/Myappoinment.html',{"appoinment":appoinment})

def mycomplaint(request):
    user=tbl_userreg.objects.get(user_id=request.session['uid'])
    complaint=tbl_complaint.objects.filter(user_id=user)
    return render(request,'User/My complaints.html',{"complaint":complaint})


def vaccination(request,id):
    pet=tbl_pet.objects.get(id=id)
    vaccine=tbl_vaccinedetails.objects.filter(pet_id=id)

    if request.method=="POST":
        name=request.POST.get('name')
        details=request.POST.get('details')
        date=request.POST.get('date')
        ndate=request.POST.get('ndate')
        tbl_vaccinedetails.objects.create(
            vaccine_name=name,vaccine_details=details,vaccine_date=date,vaccine_fordate=ndate,pet_id=pet
        )
        return render(request,'User/Vaccination.html',{"vaccine":vaccine})
    else:
        return render(request,'User/Vaccination.html',{"vaccine":vaccine})


def breedfind(request):
    return render(request,'User/breedFind.html')



    