from rest_framework import serializers
from .models import TeachersModel

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeachersModel
        fields=['id', 'firstName', 'lastName', 'dob', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance= self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

        