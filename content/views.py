from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import contentSerializer
from .models import contentModel
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext as _

class AddContent(GenericAPIView):
    serializer_class= contentSerializer
    def post(self, request):
        token= request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('User not Authenticated')

        serializer= contentSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class DeleteContent(GenericAPIView):
    serializer_class=contentSerializer
    def delete(self, request):
        id = request.data['id']
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("user not authenticated")

        if not contentModel.objects.filter(id=id).delete():
            return Response({
                "message": "failed to delete content"
            })

        return Response({
                "message": "deleted content"
            })

class GetContent(GenericAPIView):
    serializer_class= contentSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("user not authenticated")

        content= contentModel.objects.all()

        serializer = contentSerializer(content, many=True)

        return Response(serializer.data)
        
class translate(GenericAPIView):
    def get(self, request):
        text = request.data['text']
        return Response({
            "translation": _(text)
        })