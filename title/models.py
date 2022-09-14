from django.db import models

class TitleModel(models.Model):
    titleName= models.CharField(max_length=255)
    titleIcon= models.CharField(max_length=255)
    contentId= models.IntegerField()
