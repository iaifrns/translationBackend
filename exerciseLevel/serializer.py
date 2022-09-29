from rest_framework import serializers
from .models import ExerciseLevelModel

class ExerciseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLevelModel
        fields = ['id', 'level']
        