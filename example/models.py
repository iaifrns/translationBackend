from django.db import models

class exampleModel(models.Model):
    question = models.CharField(max_length=255)
    word = models.CharField(max_length=255)
    audoi = models.CharField(max_length=255)
