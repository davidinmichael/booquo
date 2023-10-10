from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *

class RegisterView(APIView):
    def post(self, request):
        data = {}
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data['message'] = "Account created successfully"
            data['username'] = user.username
            data['email'] = user.email
            return Response(data, status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors)