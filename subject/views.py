from  rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import subjectSerializer
from .models import subjectModel

class addSubject(GenericAPIView):
    serializer_class= subjectSerializer
    def post(self, request):

        token= request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('not Authenticated')

        serializer= subjectSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

class getSubjects(GenericAPIView):
    serializer_class= subjectSerializer
    def get(self, request):

        token= request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('not Authenticated')

        subject = subjectModel.objects.all()

        serializer= subjectSerializer(subject, many=True)

        return Response(serializer.data)

class deleteSubject(GenericAPIView):
    serializer_class= subjectSerializer
    def delete(self, request):
        token= request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('not Authenticated')

        id= request.data['id']
        if not subjectModel.objects.filter(id=id).delete():
            return Response({
                "message": "Failed"
            })

        return Response({
            "message": "Success"
        })