from rest_framework import serializers
from .models import compilteExerciseModel

class compilteExerciseSerialiizer(serializers.ModelSerializer):
    class Meta:
        model= compilteExerciseModel
        fields= ['id', 'userId', 'ExerciseId']