from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import FcategorySerializer
from .models import FcategoryModel
from rest_framework.exceptions import AuthenticationFailed


class addCategory(GenericAPIView):
    serializer_class= FcategorySerializer
    def post(self, request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not authenticated")

        serializer= FcategorySerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class deleteCategory(GenericAPIView):
    serializer_class= FcategorySerializer
    def delete(self, request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not authenticated")

        id= request.data['id']
        model = FcategoryModel.objects.filter(id=id).delete()

        if not model:
            return Response({
                "message": "Could not delete this category"
            })
        else:
            return Response({
                "message": "success"
            })

class getAllCategories(GenericAPIView):
    serializer_class= FcategorySerializer
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not authenticated")

        category = FcategoryModel.objects.all()
        serializer = FcategorySerializer(category, many= True)
        return Response(serializer.data)

class getOneCategory(GenericAPIView):
    serializer_class= FcategorySerializer
    def get(self, request):

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not authenticated")

        id = request.data['id']
        model = FcategoryModel.objects.filter(id=id).first()
        serializer= FcategorySerializer(model)
        return Response(serializer.data)