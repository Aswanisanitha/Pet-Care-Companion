from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_mail=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=40)

class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=40)


class tbl_pettype(models.Model):
    type_name=models.CharField(max_length=30)

class tbl_breed(models.Model):
    breed_name=models.CharField(max_length=30)
    pettype=models.ForeignKey(tbl_pettype,on_delete=models.CASCADE)

class tbl_food(models.Model):
    food_type=models.CharField(max_length=30)
    food_name=models.CharField(max_length=30)
    food_calories=models.CharField(max_length=30)

class tbl_activity(models.Model):
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)
    activity_name=models.CharField(max_length=30)
    activity_time=models.CharField(max_length=30)
    activity_details=models.CharField(max_length=30)

class tbl_abnormalactivity(models.Model):
    ab_name=models.CharField(max_length=39)
    ab_reason=models.CharField(max_length=30)
    ab_solution=models.CharField(max_length=30)
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)

class tbl_traning(models.Model):
    traning_name=models.CharField(max_length=30)
    traning_file=models.URLField()
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)

class tbl_foodplan(models.Model):
    breed=models.ForeignKey(tbl_breed,on_delete=models.CASCADE)
    food=models.ForeignKey(tbl_food,on_delete=models.CASCADE)
    food_quantity=models.CharField(max_length=30)

    




    
    