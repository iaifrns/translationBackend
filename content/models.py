from django.db import models

class contentModel(models.Model):
    subject_id = models.IntegerField()
    icon = models.CharField(max_length=255)
    contents = models.CharField(max_length=255)


