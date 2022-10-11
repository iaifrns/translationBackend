from django.db import models

class subjectModel(models.Model):
    subjectName= models.CharField(max_length=255)
    subjectIcon= models.CharField(max_length=255)
    subjectNameFench= models.CharField(max_length=255, default="Any")
    
