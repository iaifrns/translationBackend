from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import ExerciseLevelModel
from .serializer import ExerciseLevelSerializer
from rest_framework.exceptions import AuthenticationFailed

class addLevel(GenericAPIView):
    serializer_class = ExerciseLevelSerializer
    def post(self, request):
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")

        serializer = ExerciseLevelSerializer(data= request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getOneLevel(GenericAPIView):
    serializer_class = ExerciseLevelSerializer
    def get(self, request):
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        id = request.data['id']
        model = ExerciseLevelModel.objects.filter(id=id).first()
        serializer= ExerciseLevelSerializer(model)

        return Response(serializer.data)

class getAllLevel(GenericAPIView):
    serializer_class = ExerciseLevelSerializer
    def get(self, request):
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        model = ExerciseLevelModel.objects.all()
        serializer= ExerciseLevelSerializer(model, many=True)

        return Response(serializer.data)

class deleteLevel(GenericAPIView):
    serializer_class = ExerciseLevelSerializer
    def delete(self, request):
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        id = request.data['id']
        
        if not ExerciseLevelModel.objects.filter(id=id).first().delete():
            return Response({
                "message": "Failed",
                "status": 0
            })
        else:
            return Response({
                "message": "Success",
                "status": 1
            })