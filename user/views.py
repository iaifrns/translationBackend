from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializer import UserSerializer
from .models import UserModel
import jwt, datetime

class Register(APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserModel.objects.filter(email= email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if user.password!=password:
            raise AuthenticationFailed('Incorrect password')

        payload={
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token= jwt.encode(payload, 'secret', algorithm= 'HS256')

        response= Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data= {
            "token": token
        }

        return response

class getUser(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user= UserModel.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)