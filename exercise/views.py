from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import ExerciseSerializer
from .models import ExerciseModel
from rest_framework.exceptions import AuthenticationFailed

class addExercise(GenericAPIView):
    serializer_class = ExerciseSerializer
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        serializer= ExerciseSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getOneExercise(GenericAPIView):
    serializer_class = ExerciseSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        id = request.data['id']
        model = ExerciseModel.objects.filter(id=id).first()
        serializer= ExerciseSerializer(model)

        return Response(serializer.data)

class getAllExercise(GenericAPIView):
    serializer_class = ExerciseSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        model = ExerciseModel.objects.all()

        serializer = ExerciseSerializer(model, many = True)
        return Response(serializer.data)

class deleteExercise(GenericAPIView):
    serializer_class = ExerciseSerializer
    def delete(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        id = request.data['id']
        
        if not ExerciseModel.objects.filter(id=id).first().delete():
            return Response({
                "message": "Failed",
                "status": 0
            })
        else:
            return Response({
                "status": 1,
                "message": "Success"
            })
