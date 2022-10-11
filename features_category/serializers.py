from rest_framework import serializers
from .models import FcategoryModel

class FcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= FcategoryModel
        fields= ['id', 'name', 'subject_id']