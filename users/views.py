from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

