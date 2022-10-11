from rest_framework import serializers
from .models import FeatureModel

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model= FeatureModel
        fields=['id', 'image', 'name', 'categoryId', 'namefrench']