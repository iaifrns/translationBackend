from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import multipleChoiseModel
from .serializer import multipleChoiseSerializer
from rest_framework.exceptions import AuthenticationFailed

class addChoise(GenericAPIView):
    serializer_class= multipleChoiseSerializer
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not Authenticated")

        serializer= multipleChoiseSerializer(data= request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getOneChoise(GenericAPIView):
    serializer_class= multipleChoiseSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not Authenticated")
        id= request.data['id']
        model = multipleChoiseModel.objects.filter(id=id).first()
        serializer= multipleChoiseSerializer(model)
        return Response(serializer.data)

class getAllChoise(GenericAPIView):
    serializer_class= multipleChoiseSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not Authenticated")
        model= multipleChoiseModel.objects.all()
        serializer= multipleChoiseSerializer(model, many = True)

        return Response(serializer.data)

class deleteChoise(GenericAPIView):
    serializer_class= multipleChoiseSerializer
    def delete(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("not Authenticated")
        id= request.data['id']

        if not multipleChoiseModel.objects.filter(id=id).first().delete():
            return Response({
                "message": "Failed",
                "status": 0
            })
        else: 
            return Response({
                "message": "Success",
                "status": 1
            })