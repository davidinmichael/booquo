from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from email.message import EmailMessage
import smtplib
import ssl
import requests
import lxml
from bs4 import BeautifulSoup
from .models import Quote
from .serializers import *
import time
import random

def send_emails(receiver, body, author):
    sender = "davidinmichael@gmail.com"
    password = "trplzetkubdspzuq"

    subject = "Daily Quotes"
    context = ssl.create_default_context()

    obj = EmailMessage()
    obj["From"] = sender
    obj["To"] = receiver
    obj["subject"] = subject
    obj.set_content(f"{body}\n- {author}")
    obj.add_alternative(
        f"""
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="background-color: #311b92; font-family: Arial, sans-serif; color: #ffffff; text-align: center;">
    <div style="background-color: #673ab7; padding: 20px;">
        <h1 style="color: #ffffff;">Quote of the Day</h1>
    </div>
    <div style="padding: 20px;">
        <p>{body}</p>
        <p>- {author}</p>
    </div>
    <div style="padding: 20px;">
        <a href="https://twitter.com/davidinmichael" style="background-color: #673ab7; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin-right: 10px;">Twitter</a>
        <a href="https://linkedin.com/in/davidinmichael" style="color: #ffffff; text-decoration: none;">Linkedin</a>
    </div>
</body>
</html>
""", subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, obj.as_string())

class Quotes(APIView, PageNumberPagination):
    def get(self, request):
        all_quotes = Quote.objects.all()
        response = self.paginate_queryset(all_quotes, request, view=self)
        serializer = QuoteSerializer(response, many=True)
        return self.get_paginated_response(serializer.data)

class SingleQuote(APIView):
    def get(self, request, id):
        try:
            quote = Quote.objects.get(id=id)
        except Quote.DoesNotExist:
            return Response({"message": "Oops, Quote not found"}, status.HTTP_404_NOT_FOUND)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status.HTTP_200_OK)


class AllAuthors(APIView):
    def get(self, request):
        authors = Quote.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SendQuotes(APIView):
    def quote_handle(self):
        quote_list = Quote.objects.all()
        users = User.objects.all()
        
        for user in users:
            random_quote = random.choice(quote_list)
            send_emails(user.email, random_quote.quote, random_quote.author)
        time.sleep(30)
        self.quote_handle()

    def get(self, request):
        self.quote_handle()
        return Response({"message": "Daily Quotes in Progress"})