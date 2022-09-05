from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    firstName= models.CharField(max_length=30)
    lastName= models.CharField(max_length=30)
    dob= models.CharField(max_length=30)
    email= models.CharField(max_length=30, unique= True)
    password= models.CharField(max_length=30)
    username= None

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
