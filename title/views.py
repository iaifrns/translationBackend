from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import TitleSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import TitleModel

class AddTitle(GenericAPIView):
    serializer_class=TitleSerializer
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Not authenticated")

        serializer= TitleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class GetTitles(GenericAPIView):
    serializer_class= TitleSerializer
    def get(self, request):
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not authenticated")

        titles= TitleModel.objects.all()
        serializer= TitleSerializer(titles, many=True)

        return Response(serializer.data)

class DeleteTitle(GenericAPIView):
    serializer_class= TitleSerializer
    def delete(self, request):
        id= request.data['id']
        token= request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Not authenticated")

        if not TitleModel.objects.filter(id=id).delete():
            return Response({
                "message": "Failed"
            })
        return Response({
                "message": "Success"
            })

