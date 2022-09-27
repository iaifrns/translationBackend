from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import FeatureSerializer
from .models import FeatureModel
from rest_framework.exceptions import AuthenticationFailed

class addFeature(GenericAPIView):
    serializer_class = FeatureSerializer
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not Authentication")
        serializer= FeatureSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getOneFeature(GenericAPIView):
    serializer_class = FeatureSerializer
    def get(self, request):
        id = request.data['id']
        model= FeatureModel.objects.filter(id=id).first()
        serializer= FeatureSerializer(model)

        return Response(serializer.data)

class getAllFeatures(GenericAPIView):
    serializer_class = FeatureSerializer
    def get(self, request):
        model = FeatureModel.objects.all()
        serializer= FeatureSerializer(model, many= True)

        return Response(serializer.data)

class deleteFeature(GenericAPIView):
    serializer_class = FeatureSerializer
    def delete(self, request):
        id= request.data['id']
        model = FeatureModel.objects.filter(id=id).delete()

        if not model:
            return Response({
                "message": "Failed to delete the Feature",
                "status": 0
            })
        else:
            return Response({
                "message": "Success",
                "status": 1
            })
        
