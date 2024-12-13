from django.db import models
from Admin.models import*
from Guest.models import*
from Vetinaryhospital.models import *



# Create your models here.

class tbl_pet(models.Model):
    pet_name=models.CharField(max_length=30)
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)
    pet_weight=models.CharField(max_length=30)
    pet_photo=models.URLField()
    pet_age=models.CharField(max_length=30)
    pet_gender=models.CharField(max_length=30)
    user_id=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=300)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=200)
    user_id=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    complaint_status=models.IntegerField(default=0)


class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)

class tbl_appoinment(models.Model):
    user_id=models.ForeignKey(tbl_userreg,on_delete=models.CASCADE)
    slot=models.ForeignKey(tbl_slot,on_delete=models.CASCADE)
    appoinment_date=models.DateField(auto_now_add=True)
    appoinment_Fordate=models.DateField()
    appoinment_status=models.IntegerField(default=0)
    appoinment_token=models.IntegerField(null=True)

class tbl_gallery(models.Model):
    pet_id=models.ForeignKey(tbl_pet,on_delete=models.CASCADE)
    gallery_title=models.CharField(max_length=30)
    gallery_file=models.URLField()
    gallery_date=models.DateField(auto_now_add=True)

class tbl_vaccinedetails(models.Model):
    vaccine_name=models.CharField(max_length=30)
    vaccine_details=models.CharField(max_length=30)
    vaccine_date=models.DateField()
    vaccine_fordate=models.DateField()
    pet_id=models.ForeignKey(tbl_pet,on_delete=models.CASCADE)









