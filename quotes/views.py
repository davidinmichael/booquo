from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from email.message import EmailMessage
import smtplib
import ssl
import requests
import lxml
from bs4 import BeautifulSoup
from .models import Quote
from .serializers import *

def send_emails(receiver, body):
    sender = "davidinmichael@gmail.com"
    password = "trplzetkubdspzuq"

    subject = "Daily Quotes"
    context = ssl.create_default_context()

    obj = EmailMessage()
    obj["From"] = sender
    obj["To"] = receiver
    obj["subject"] = subject
    obj.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, obj.as_string())

class Quotes(APIView, PageNumberPagination):
    def get(self, request):

        # All books were scrapped, with the information below

        # for i in range(1, 11):
        #     response = requests.get(f"http://quotes.toscrape.com/page/{i}/")
        #     soup = BeautifulSoup(response.text, "lxml")

        #     quotes = soup.select(".text")
        #     quote_s = [quote.text for quote in quotes]

        #     authors = soup.select(".author")
        #     author_s = [author.text for author in authors]

        #     for item in range(len(author_s)):
        #         Quote.objects.create(author=author_s[item], quote=quote_s[item])
        
        all_quotes = Quote.objects.all()
        response = self.paginate_queryset(all_quotes, request, view=self)
        serializer = QuoteSerializer(response, many=True)
        return self.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

class SingleQuote(APIView):
    def get(self, request, id):
        try:
            quote = Quote.objects.get(id=id)
        except Quote.DoesNotExist:
            return Response({"message": "Oops, Quote not found"}, status.HTTP_404_NOT_FOUND)
        # message = f"{quote.quote}\nby {quote.author}"
        # send_emails("ilightwears@gmail.com", message)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status.HTTP_200_OK)


class AllAuthors(APIView):
    def get(self, request):
        # authors = Quote.objects.values_list("author", flat=True)
        authors = Quote.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)