from django.db import models

# Create your models here.

class catdata(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    profileimg = models.ImageField(upload_to="media",null=True,blank=True)  

class proddb(models.Model):
    catname = models.CharField(max_length=100,null=True,blank=True)
    proname = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    price =  models.IntegerField(null=True,blank=True)
    productimage  = models.ImageField(upload_to="media",null=True,blank=True)
