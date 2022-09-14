from django.db import models

class ExampleModel(models.Model):
    question = CharField(max_length=255)
    
