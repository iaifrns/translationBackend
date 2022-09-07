from django.db import models

class contentModel(models.Model):
    subject_id = models.IntegerField()
    contents = models.CharField(max_length=255)


