from django.shortcuts import render, redirect
from Guest.models import *
import uuid

# Create your views here.


def homepage(request):
    return render(request,'Vetinaryhospital/Homepage.html')

def myprofile(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["uid"])
    return render(request,'Vetinaryhospital/Myprofile.html',{"vhosptl":vhosptl})


def editprofile(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["uid"])
    if request.method=="POST":
        vhosptl.vetinaryhospital_name=request.POST.get('name')
        vhosptl.vetinaryhospital_email=request.POST.get('email')
        vhosptl.vetinaryhospital_contact=request.POST.get('Contact')
        vhosptl.vetinaryhospital_address=request.POST.get('address')
        vhosptl.save()
        return redirect('Vetinaryhospital:myprofile')
    else:
         return render(request,'Vetinaryhospital/Editprofile.html',{"vhosptl":vhosptl})


def changepassword(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["uid"])
    if request.method=="POST":
        pswd=vhosptl.vetinaryhospital_password
        oldpswd=request.POST.get('oldpswd')
        newpswd=request.POST.get('newpswd')
        repswd=request.POST.get('repswd')
        if pswd==oldpswd:
            if newpswd == repswd:
                vhosptl.vetinaryhospital_password=newpswd
                vhosptl.save()
                return redirect('Vetinaryhospital:myprofile')
            else:
                return render(request,'Vetinaryhospital/changepassword.html',{'error':"Different Password"})
        else:
            return render(request,'Vetinaryhospital/changepassword.html',{'error':"Invalid Password"})
    else:
        return render(request,'Vetinaryhospital/Changepassword.html')
