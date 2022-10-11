from django.db import models

class ExerciseModel(models.Model):
    question = models.CharField(max_length=255)
    questionfrench= models.CharField(max_length=255, default="Any")
    ans = models.CharField(max_length=255)
    levelId= models.IntegerField()
    status = models.CharField(max_length=255)
