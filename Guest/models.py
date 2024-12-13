from django.db import models
from Admin.models import *
import uuid

# Create your models here.
class tbl_userreg(models.Model):
    user_id = models.TextField(primary_key=True, editable=False) 
    user_name=models.CharField(max_length=40)
    user_address=models.CharField(max_length=40)
    user_contact=models.CharField(max_length=40)
    user_email=models.CharField(max_length=40)
    user_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.URLField()
    user_gender=models.CharField(max_length=40)
    user_dob=models.DateField ()
    user_password=models.CharField(max_length=40)


class tbl_vetinaryhospital(models.Model):
    vetinaryhospital_id = models.TextField(primary_key=True, editable=False) 
    vetinaryhospital_name=models.CharField(max_length=40)
    vetinaryhospital_email=models.CharField(max_length=40)
    vetinaryhospital_contact=models.CharField(max_length=40)
    vetinaryhospital_address=models.CharField(max_length=40)
    place_id=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    vetinaryhospital_proof=models.URLField()
    vetinaryhospital_password=models.CharField(max_length=40)
    vetinaryhospital_status=models.IntegerField(default=0)


    