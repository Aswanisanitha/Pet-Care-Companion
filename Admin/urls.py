from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    path('Sum/',views.sum,name="sum"),
    path('Add/',views.add,name="add"),
    path('Salary/',views.salary,name="salary"),
    path('District/',views.district,name="district"),
    path('Category/',views.category,name="category"),
    path('Admin/',views.Admin,name="Admin"),
    path('deladmin/<str:id>',views.deladmin,name="deladmin"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
    path('editadmin/<str:id>',views.editadmin,name="editadmin"),
    path('Place/',views.place,name="place"),
    path('Subcategory/',views.subcategory,name="subcategory"),
    path('editsubcategory/<int:id>',views.editsubcategory,name="editsubcategory"),


    path('Homepage/',views.homepage,name="homepage"),


    path('Pettype/',views.pettype,name="pettype"),
    path('deltype/<int:id>',views.deltype,name="deltype"),
    path("Breed/",views.breed,name="breed"),
    path('delbreed/<int:id>',views.delbreed,name="delbreed"),
    path('Food/',views.food,name="food"),
    path('delfood/<int:id>',views.delfood,name="delfood"),
    path('Activity/',views.activity,name="activity"),
    path('Ajaxbreed/',views.ajaxbreed,name="ajaxbreed"),
    path('delactivity/<int:id>',views.delactivity,name="delactivity"),
    path('Abnormalactivity/',views.abnormalactivity,name="abnormalactivity"),
    path('delabnormalactivity/<int:id>',views.delabnormalactivity,name="delabnormalactivity"),
    path('Traning/',views.traning,name="traning"),
    path('deltraning/<int:id>',views.deltraning,name="deltraning"),
    path('Foodplan/',views.foodplan,name="foodplan"),


    path('Hospital/',views.hospital,name="hospital"),
    path('accept/<str:aid>',views.accept,name="accept"),
    path('reject/<str:rid>',views.reject,name="reject"),



]