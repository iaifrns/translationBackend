from django.db import models

class ExerciseModel(models.Model):
    question = models.CharField(max_length=255)
    ans = models.CharField(max_length=255)
    levelId= models.IntegerField()
    status = models.CharField(max_length=255)
