from django.urls import path
from Vetinaryhospital import views
app_name="Vetinaryhospital"

urlpatterns = [
    path('Homepage/',views.homepage,name="homepage"),
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),


    path('Appointments/',views.appointments,name="appointments"),
    

    path('Slot/',views.slot,name="slot"),
    path('delslot/<int:id>',views.delslot,name="delslot"),


    


 
]