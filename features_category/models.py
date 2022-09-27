from django.db import models

class FcategoryModel(models.Model):
    name = models.CharField(max_length=255)
