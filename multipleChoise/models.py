from django.db import models

class multipleChoiseModel(models.Model):
    answer = models.CharField(max_length=255)
    execiseId= models.IntegerField()
    