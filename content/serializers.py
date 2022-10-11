from rest_framework import serializers
from .models import contentModel

class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model= contentModel
        fields= ['id', 'subject_id', 'icon', 'contents', 'contentfrench']
