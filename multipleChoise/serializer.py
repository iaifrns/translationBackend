from rest_framework import serializers
from .models import multipleChoiseModel

class multipleChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model= multipleChoiseModel
        fields = ['id', 'answer', 'execiseId']
