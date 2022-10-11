from django.db import models

class FcategoryModel(models.Model):
    name = models.CharField(max_length=255)
    subject_id= models.IntegerField(default=1)