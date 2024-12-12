from django.shortcuts import render, redirect
from Guest.models import *
from User.models import *
from Vetinaryhospital.models import *


# Create your views here.


def homepage(request):
    return render(request,'Vetinaryhospital/Homepage.html')

def myprofile(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["vid"])
    return render(request,'Vetinaryhospital/Myprofile.html',{"vhosptl":vhosptl})


def editprofile(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["vid"])
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
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session["vid"])
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



def appointments(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session['vid'])
    appointment=tbl_appoinment.objects.filter(slot__vetinaryhospital_id=vhosptl)
    
    return render(request,'Vetinaryhospital/Appoinments.html',{"appointment":appointment})




def slot(request):
    vhosptl=tbl_vetinaryhospital.objects.get(vetinaryhospital_id=request.session['vid'])
    slot=tbl_slot.objects.filter(vetinaryhospital_id=vhosptl)
    print(slot)
    if request.method=="POST":
        ftime=request.POST.get('fromtime')
        ttime=request.POST.get('totime')
        count=request.POST.get('slotcount')
        tbl_slot.objects.create(
            slot_fromtime=ftime,slot_totime=ttime,slot_count=count,vetinaryhospital_id=vhosptl
        )
        return redirect("Vetinaryhospital:slot")
    else:
        return render(request,'Vetinaryhospital/Slot.html',{'slot':slot})



def delslot(request,id):
    tbl_slot.objects.get(id=id).delete()
    return redirect("Vetinaryhospital:slot")







