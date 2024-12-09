from django.shortcuts import render, redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.conf import settings
from supabase import create_client
import uuid
# Create your views here.



supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

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
    pet=tbl_pet.objects.all()
    # print(pet)
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
        # tbl_feedback.objects.create(
        #     feedback_content=content,feedback_date= ,user_id=user
        # )
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

# def ajaxplace(request):
#     pettype=request.GET.get("pid")
#     breed=request.GET.get("did")
#     abactivity=tbl_abnormalactivity.objects.filter(breed=breed,breed__pettype__id=pettype)
#     return render(request,'User/Ajaxplace.html',{'abactivity':abactivity})

def ajaxplace(request):
    district_id = request.GET.get('did')
    place = tbl_place.objects.filter(district=district_id)
    return render(request, "User/Ajaxplace.html", {'place': place})
    










    