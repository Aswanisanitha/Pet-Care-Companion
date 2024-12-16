from django.urls import path
from User import views

app_name="User"


urlpatterns = [
    
    path('Homepage/',views.homepage,name="homepage"),
    path('Myprofile/',views.myprofile,name="myprofile"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('Changepassword/',views.changepassword,name="changepassword"),

    path('Pet/',views.pet,name="pet"),
    path('Ajaxbreed/',views.ajaxbreed,name="ajaxbreed"),
    path('delpet/<int:id>',views.delpet,name="delpet"),
    path('gallery/<int:id>',views.gallery,name="gallery"),
    path('delgallery/<int:id>',views.delgallery,name="delgallery"),
    path('Viewpets/',views.viewpets,name="viewpets"),
    path('Viewgallery/<int:id>',views.viewgallery,name="viewgallery"),



    path('Complaint/',views.complaint,name="complaint"),
    path('delcomplaint/<int:id>',views.delcomplaint,name="delcomplaint"),

    path('Feedback/',views.feedback,name="feedback"),
    path('delfeedback/<int:id>',views.delfeedback,name="delfeedback"),

    path('training/',views.training,name="training"),
    path('ajaxtraining/',views.ajaxtraining,name="ajaxtraining"),

    path('ajaxfood/',views.ajaxfood,name="ajaxfood"),
    path('food/',views.food,name="food"),

    path('ajaxactivity/',views.ajaxactivity,name="ajaxactivity"),
    path('Activity/',views.activity,name="activity"),

    path('ajaxabactivity/',views.ajaxabactivity,name="ajaxabactivity"),
    path('abnormalactivity/',views.abnormalactivity,name="abnormalactivity"),

    path('ajaxhospital/',views.ajaxhospital,name="ajaxhospital"),
    path('vetinaryhospital/',views.vetinaryhospital,name="vetinaryhospital"),

    path('Myappoinment/',views.myappoinment,name="myappoinment"),
    
    path('slot/<str:id>',views.slot,name="slot"),
    path('Mycomplaint/',views.mycomplaint,name="mycomplaint"),


    path('Vaccination/<int:id>',views.vaccination,name="vaccination"),

    path('predict_image/',views.predict_image,name="predict_image"),


    





]