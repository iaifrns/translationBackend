from  rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import compilteExerciseSerialiizer
from .models import compilteExerciseModel

class addComplitedExercise(GenericAPIView):
    serializer_class = compilteExerciseSerialiizer
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        serializer= compilteExerciseSerialiizer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getOneComplitedExercise(GenericAPIView):
    serializer_class = compilteExerciseSerialiizer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        id= request.data['id']
        model = compilteExerciseModel.objects.filter(id= id).first()

        serializer= compilteExerciseSerialiizer(model)
        return Response(serializer.data)

class getAllCompliteExercise(GenericAPIView):
    serializer_class = compilteExerciseSerialiizer
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not Authenticated")
        model = compilteExerciseModel.objects.all()
        serializer= compilteExerciseSerialiizer(model, many=True)

        return Response(serializer.data)
