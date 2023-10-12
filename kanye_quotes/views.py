from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class KanyeQuotes(APIView):
    def get(self, request):
        url = "https://api.kanye.rest/"
        response = requests.get(url).json()
        return Response(response, status.HTTP_200_OK)
