from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from django.conf import settings
from supabase import create_client
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
# Create your views here.



supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def index(request):
    return render(request,'Guest/Index.html')

def userreg(request):
    dis = tbl_district.objects.all()
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            print(auth_response.user)

            
            if auth_response.user:
                user_data = auth_response.user  
                user_id = user_data.id
                photo = request.FILES.get('photo')

                if photo:
                    try:
                        # File name uses only user_id and the original photo name
                        file_name = f"UserDocs/{user_id}_{photo.name}"
                        photo_content = photo.read()
                        storage_response = supabase.storage.from_("petcare").upload(file_name, photo_content)
                        photo_url = supabase.storage.from_("petcare").get_public_url(file_name)
                    except Exception as e:
                        return render(request, "Guest/UserRegistration.html", {"district": dis, "error": "Failed to upload photo."})
                else:
                    photo_url = None  # Handle cases where no photo is uploaded
                
                # Save user details in the database
                tbl_userreg.objects.create(
                    user_id=user_id,
                    user_name=request.POST.get('name'),
                    user_email=email,
                    user_password=password,
                    user_address=request.POST.get('address'),
                    user_contact=request.POST.get('contact'),
                    user_gender=request.POST.get('gender'),
                    user_dob=request.POST.get('dob'),
                    user_photo=photo_url,
                    user_place=tbl_place.objects.get(id=request.POST.get('place'))
                )
                
                return redirect('Guest:login')
            else:
                return render(request, "Guest/UserRegistration.html", {"district": dis, "error": "Sign-up failed."})

        except Exception as e:
            # print(e)
            return render(request, "Guest/UserRegistration.html", {"district": dis, "error": "An error occurred during sign-up."})
    else:
        return render(request, "Guest/UserRegistration.html", {"district": dis})

def ajaxplace(request):
    district_id = request.GET.get('did')
    place = tbl_place.objects.filter(district=district_id)
    return render(request, "Guest/AjaxPlace.html", {'place': place})


def login(request):
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user with Supabase
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if auth_response.user:
            user_data = auth_response.user
            user_id = user_data.id
            print(user_id)

            try:
                # Check in tbl_userreg
                user = tbl_userreg.objects.get(user_id=user_id)
                request.session['uid'] = user.user_id
                send_vaccine_reminders(user)
                return redirect("User:homepage")
            except tbl_userreg.DoesNotExist:
                try:
                    # Check in tbl_vetinaryhospital
                    hospital = tbl_vetinaryhospital.objects.get(vetinaryhospital_id=user_id)
                    request.session['vid'] = hospital.vetinaryhospital_id
                    return redirect("Vetinaryhospital:homepage")
                except tbl_vetinaryhospital.DoesNotExist:
                    try:
                        admin = tbl_admin.objects.get(admin_id=user_id)
                        request.session['aid'] = admin.admin_id
                        return redirect("Admin:homepage")
                    except tbl_admin.DoesNotExist:
                    # Neither user nor hospital found
                       return render(request, "Guest/Login.html", {"error": "User does not exist"})
        else:
            # Invalid authentication
            return render(request, "Guest/Login.html", {"error": "Invalid credentials"})
    else:
        # For non-POST requests
        return render(request, 'Guest/Login.html')





def send_vaccine_reminders(user):
    """
    Sends email reminders for vaccines scheduled for tomorrow.
    """
    tomorrow = timezone.now().date() + timedelta(days=1)

    # Check for vaccines scheduled tomorrow for the logged-in user
    reminders = tbl_vaccinedetails.objects.filter(
        pet_id__user=user,  # Ensure the pet belongs to the logged-in user
        vaccine_fordate=tomorrow
    )

    for reminder in reminders:
        subject = "Vaccine Reminder for Your Pet"
        body = f"""
        Dear {user.user_name},

        This is a reminder about your pet's vaccination:
        Vaccine Name: {reminder.vaccine_name}
        Vaccine Details: {reminder.vaccine_details}
        Scheduled Date: {reminder.vaccine_fordate}

        Please ensure your pet gets the vaccine on time.

        Regards,
        Pet Care Companion Team
        """

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,  # Sender's email from settings
            [user.user_email],         # Recipient's email
            fail_silently=False,
        )



def vetinaryhospital(request):
    dis = tbl_district.objects.all()
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            print(auth_response.user)

            
            if auth_response.user:
                user_data = auth_response.user  
                user_id = user_data.id
                photo = request.FILES.get('photo')

                if photo:
                    try:
                        # File name uses only user_id and the original photo name
                        file_name = f"HospitalDocs/{photo.name}"
                        photo_content = photo.read()
                        storage_response = supabase.storage.from_("petcare").upload(file_name, photo_content)
                        photo_url = supabase.storage.from_("petcare").get_public_url(file_name)
                    except Exception as e:
                        return render(request, "Guest/Vetinaryhospital.html", {"district": dis, "error": "Failed to upload photo."})
                else:
                    photo_url = None  # Handle cases where no photo is uploaded
                
                
                tbl_vetinaryhospital.objects.create(
                    vetinaryhospital_id=user_id,
                    vetinaryhospital_name=request.POST.get('name'),
                    vetinaryhospital_email=email,
                    vetinaryhospital_password=password,
                    vetinaryhospital_address=request.POST.get('address'),
                    vetinaryhospital_contact=request.POST.get('contact'),
                    
                    vetinaryhospital_proof=photo_url,
                    place_id=tbl_place.objects.get(id=request.POST.get('place'))
                )
                
                return redirect('Guest:login')
            else:
                return render(request, "Guest/Vetinaryhospital.html", {"district": dis, "error": "Sign-up failed."})

        except Exception as e:
           
            return render(request, "Guest/Vetinaryhospital.html", {"district": dis, "error": "An error occurred during sign-up."})
    else:
        return render(request, "Guest/Vetinaryhospital.html", {"district": dis})
