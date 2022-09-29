from django.db import models

class compilteExerciseModel(models.Model):
    userId = models.IntegerField()
    ExerciseId = models.IntegerField()
