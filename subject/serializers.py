from rest_framework import serializers
from .models import subjectModel

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= subjectModel
        fields=['id', 'subjectName', 'subjectIcon']