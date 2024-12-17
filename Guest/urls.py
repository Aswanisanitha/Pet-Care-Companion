from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('',views.index,name="index"),
    
    path('Userreg/',views.userreg,name="userreg"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.login,name="login"),


    path('Vetinaryhospital/',views.vetinaryhospital,name="vetinaryhospital"),



 
]