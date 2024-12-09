from django.shortcuts import render,redirect
from Admin.models import *
from django.conf import settings
from supabase import create_client
import uuid
# Create your views here.



supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
def sum(request):
    if request.method=="POST":
        Num1=int(request.POST.get('number1'))
        Num2=int(request.POST.get('number2'))
        btn=request.POST.get('btn')
        if btn=="+":
            Result=Num1+Num2
        elif btn=="-":
            Result=Num1-Num2
        elif btn=="*":
            Result=Num1*Num2
        elif btn=="/":
            Result=Num1/Num2
        return render(request,'Admin/Sum.html',{'result':Result})
    else:
        return render(request,'Admin/Sum.html')

def add(request):
    if request.method=="POST":
        Num1=int(request.POST.get('number1'))
        Num2=int(request.POST.get('number2'))
        Num3=int(request.POST.get('number3'))
        if (Num1>Num2)&(Num1>Num3):
            largest=Num1
        elif (Num2>Num1)&(Num2>Num3):
            largest=Num2
        elif(Num3>Num1)&(Num3>Num2):
            largest=Num3

        if (Num1<Num2)&(Num1<Num3):
            smallest=Num1            
        elif (Num2<Num1)&(Num2<Num3):
            smallest=Num2
        elif(Num3<Num1)&(Num3<Num2):
            smallest=Num3
              
        return render(request,'Admin/Add.html',{'result':largest,'smallest':smallest})
    else:
        return render(request,'Admin/Add.html')

def salary(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        martial=request.POST.get('martial')
        dept=request.POST.get('sel_dept')
        salary=int(request.POST.get('salary'))
        btn=request.POST.get('btn')
        fulname=fname+ ' ' +lname
        if gender=="male":
            name='Mr.'+fulname
        elif gender=="female" and martial=="single":
            name='Ms.'+fulname
        elif gender=="female" and martial=="married":
            name='Mrs.'+fulname
        if (salary >= 25000):
            ta=0.4*salary
            da=0.35*salary
            hra=0.3*salary
            lic=0.25*salary
            pf=0.2*salary
        elif (salary >= 15000)&(salary<25000):
            ta=0.35*salary
            da=0.3*salary
            hra=0.25*salary
            lic=0.2*salary
            pf=0.15*salary
        elif (salary >= 15000):
            ta=0.3*salary
            da=0.25*salary
            hra=0.2*salary
            lic=0.15*salary
            pf=0.1*salary
        Deduction=lic+pf
        net=salary+ta+da+hra-(Deduction)
        return render(request,'Admin/Salary.html',{'name':name,'gender':gender,'martial':martial,'dept':dept,'salary':salary,'ta':ta,'da':da,'hra':hra,'lic':lic,'pf':pf,'deduction':Deduction,'net':net})
    else:
        return render(request,'Admin/Salary.html')

def district(request):
    dis=tbl_district.objects.all()

    if request.method=="POST":
        district=request.POST.get("district")
        tbl_district.objects.create(district_name=district)
        # return redirect("Admin:district")
        return render(request,'Admin/District.html',{'msg':"Data Inserted Successfilly",'district':dis})

    else:
        return render(request,'Admin/District.html',{'district':dis})


def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")


def editdistrict(request,id):
    dis=tbl_district.objects.get(id=id)
    if request.method=="POST":
        district=request.POST.get("district")
        dis.district_name=district

        dis.save()
        return redirect("Admin:district")
    else:
        return render(request,'Admin/District.html',{'editdata':dis})



def category(request):
    if request.method=="POST":
        category=request.POST.get("category")
        tbl_category.objects.create(category_name=category)
        msg="data Inserted"
        return render(request,'Admin/Category.html',{'msg':msg})
    else:
        return render(request,'Admin/Category.html')




def Admin(request):
    adm=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        mail=request.POST.get("email")
        pwd=request.POST.get("password")
        tbl_admin.objects.create(admin_name=name,admin_mail=mail,admin_password=pwd)
        msg="data Inserted"
        return render(request,'Admin/Admin.html',{'msg':msg,'Admin':adm})
    else:
        return render(request,'Admin/Admin.html',{'Admin':adm})

def deladmin(request,id):
    tbl_admin.objects.get(id=id).delete()
    return redirect("Admin:Admin")

def editadmin(request,id):
    ad=tbl_admin.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        mail=request.POST.get("email")
        pwd=request.POST.get("password")
        ad.admin_name=name
        ad.admin_mail=mail
        ad.admin_password=pwd

        ad.save()
        return redirect("Admin:Admin")
    else:
        return render(request,'Admin/Admin.html',{'editadmin':ad})

def place(request):
    dis=tbl_district.objects.all()
    plc=tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("district"))
        plc=request.POST.get("place")
        tbl_place.objects.create(district=district, place_name=plc )
        msg="Data Inserted"
        return render(request,'Admin/Place.html',{'msg':msg})
    else:
        return render(request,'Admin/Place.html',{'place':plc,'district':dis})
        

def subcategory(request):
    cat=tbl_category.objects.all()
    sub=tbl_subcategory.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get("Category"))
        subcategory=request.POST.get("subcategory")
        tbl_subcategory.objects.create(category=category,subcategory_name=subcategory)
        msg="data Inserted"
        return render(request,'Admin/Subcategory.html',{'msg':msg})
    else:
        return render(request,'admin/Subcategory.html',{'category':cat,'subcategory':sub})

def editsubcategory(request,id):
    cat=tbl_category.objects.all()
    sub=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        sub.category=tbl_category.objects.get(id=request.POST.get("Category"))
        
    return render(request,'admin/Subcategory.html',{'category':cat,'edit':sub})







def pettype(request):
    type=tbl_pettype.objects.all()
    if request.method=="POST":
        pettype=request.POST.get("pettype")
        tbl_pettype.objects.create(
            type_name=pettype
        )
        return render(request,'Admin/Pettype.html',{'msg':"data Inserted"})
    else:
        return render(request,'Admin/Pettype.html',{'type':type})

def deltype(request,id):
    tbl_pettype.objects.get(id=id).delete()
    return redirect("Admin:pettype")

def breed(request):
    type=tbl_pettype.objects.all()
    breed=tbl_breed.objects.all()
    if request.method=="POST":
        pettype=tbl_pettype.objects.get(id=request.POST.get("pettype"))
        breed=request.POST.get("breed")
        tbl_breed.objects.create(
            breed_name=breed,pettype=pettype
        )
        return render(request,'Admin/Breed.html',{'msg':"data Inserted"})
    else:
        return render(request,'Admin/Breed.html',{'breed':breed,'type':type})

def delbreed(request,id):
    tbl_breed.objects.get(id=id).delete()
    return redirect("Admin:breed")

def food(request):
    food=tbl_food.objects.all()
    if request.method=="POST":
        foodname=request.POST.get("foodname")
        foodtype=request.POST.get("type")
        calories=request.POST.get("calories")
        tbl_food.objects.create(food_type=foodtype,food_name=foodname,food_calories=calories)
        return render(request,'Admin/Food.html',{'msg':"data Inserted"})
    else:
        return render(request,'Admin/Food.html',{'food':food})


def delfood(request,id):
    tbl_food.objects.get(id=id).delete()
    return redirect("Admin:food")

def activity(request):
    pettype=tbl_pettype.objects.all()
    act=tbl_activity.objects.all()
    if request.method=="POST":
        activityname=request.POST.get("activityname")
        time=request.POST.get("time")
        details=request.POST.get("details")
        tbl_activity.objects.create(
            breed=tbl_breed.objects.get(id=request.POST.get('breed')),
            activity_name=activityname,activity_time=time,activity_details=details
        )
        return render(request,'Admin/Activity.html',{'msg':"Data inserted"})
    else:
        return render(request,'Admin/Activity.html',{'act':act,'type':pettype})

def ajaxbreed(request):
    type_id= request.GET.get('did')
    breed = tbl_breed.objects.filter(pettype=type_id)
    return render(request, "Admin/Ajaxbreed.html", {'breed': breed})

def delactivity(request,id):
    tbl_activity.objects.get(id=id).delete()
    return redirect("Admin:activity")


def abnormalactivity(request):
    pettype=tbl_pettype.objects.all()
    abactivity=tbl_abnormalactivity.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        reason=request.POST.get("reason")
        solution=request.POST.get("solution")
        tbl_abnormalactivity.objects.create(
            breed=tbl_breed.objects.get(id=request.POST.get('breed')),
            ab_name=name,ab_reason=reason,ab_solution=solution)
        return render(request,'Admin/Abnormalactivity.html',{'msg':"Data inserted"})
    else:
        return render(request,'Admin/Abnormalactivity.html',{'abactivity':abactivity,'type':pettype})



def ajaxbreed(request):
    type_id= request.GET.get('did')
    breed = tbl_breed.objects.filter(pettype=type_id)
    return render(request, "Admin/Ajaxbreed.html", {'breed': breed})

def delabnormalactivity(request,id):
    tbl_abnormalactivity.objects.get(id=id).delete()
    return redirect("Admin:abnormalactivity")
        

def ajaxbreed(request):
    type_id= request.GET.get('did')
    breed = tbl_breed.objects.filter(pettype=type_id)
    return render(request, "Admin/Ajaxbreed.html", {'breed': breed})

def deltraning(request,id):
    tbl_traning.objects.get(id=id).delete()
    return redirect("Admin:traning")

def traning(request):
    pettype=tbl_pettype.objects.all()
    traning=tbl_traning.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        photo=request.FILES.get("photo")


        if photo:
            try:
                # File name uses only user_id and the original photo name
                file_name = f"Traningvideos/{photo.name}"
                photo_content = photo.read()
                storage_response = supabase.storage.from_("petcare").upload(file_name, photo_content)
                photo_url = supabase.storage.from_("petcare").get_public_url(file_name)
            except Exception as e:
                print(e)
                return render(request, "Admin/Traning.html", { "error": "Failed to upload photo."})
        else:
            photo_url = None  # Handle cases where no photo is uploaded
        tbl_traning.objects.create(
            breed=tbl_breed.objects.get(id=request.POST.get('breed')),
            traning_name=name,traning_file=photo_url
        )
        return render(request,'Admin/Traning.html',{'msg':"Data inserted"})
    else:
        return render(request,'Admin/Traning.html',{'traning':traning,'type':pettype})


def foodplan(request):
    pettype=tbl_pettype.objects.all()
    foodplan=tbl_foodplan.objects.all()
    food=tbl_food.objects.all()
    if request.method=="POST":
        quantity=request.POST.get("quantity")
        
        tbl_foodplan.objects.create(
            breed=tbl_breed.objects.get(id=request.POST.get('breed')),
            food_quantity=quantity,food=tbl_food.objects.get(id=request.POST.get('food')),

        )

        return render(request,'Admin/Foodplan.html',{'msg':"Data inserted"})
    else:
        return render(request,'Admin/Foodplan.html',{'foodplan':foodplan,'pettype':pettype,'food':food})
    
        
              
    







