from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from email.message import EmailMessage
import smtplib
import ssl
import requests
import lxml
import bs4
from .models import Book
from .serializers import *


class Books(APIView, PageNumberPagination):
    def get(self, request):
        books_data = Book.objects.all()
        response = self.paginate_queryset(books_data, request, view=self)
        serializer = BookSerializer(response, many=True)

        data = {
            "message": "Books retrieved successfully!",
            "status_code": status.HTTP_200_OK,
            "books": serializer.data,
        }

        return self.get_paginated_response(data)

class SingleBook(APIView):

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": "Oops, Book not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)