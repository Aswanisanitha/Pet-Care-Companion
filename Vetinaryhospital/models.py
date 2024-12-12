from django.db import models
from Admin.models import*
from Guest.models import*

# Create your models here.

class tbl_slot(models.Model):
    slot_fromtime=models.TimeField()
    slot_totime=models.TimeField()
    slot_count=models.CharField(max_length=20)
    vetinaryhospital_id=models.ForeignKey(tbl_vetinaryhospital,on_delete=models.CASCADE)