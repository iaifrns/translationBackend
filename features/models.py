from django.db import models

class FeatureModel(models.Model):
    image= models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    namefrench = models.CharField(max_length=255, default="Any")
    categoryId= models.IntegerField()

