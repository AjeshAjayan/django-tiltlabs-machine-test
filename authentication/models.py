from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length= 70, default= '', unique= True)
    password = models.CharField(max_length= 70, default= '')
    firstname = models.CharField(max_length=50, default= '')
    lastname = models.CharField(max_length=50, default= '')
