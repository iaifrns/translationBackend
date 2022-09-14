from rest_framework import serializers
from .models import TitleModel

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model= TitleModel
        fields= ['id', 'titleName', 'titleIcon', 'contentId']