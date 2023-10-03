from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import lxml
import bs4
from .models import Book
from .serializers import *

class Books(APIView):

    def get(self, request):
        # Books and info were scrapped with the below information

        # books_and_prices = []
        # books_list = []

        # for i in range(1, 51):
        #     response = requests.get(f"http://books.toscrape.com/catalogue/page-{i}.html")
        #     data = response.text
        #     soup = bs4.BeautifulSoup(data, "lxml")

        #     title = soup.select("article h3")
        #     titles = []
        #     for item in title:
        #         titles.append(item.text)

        #     price = soup.select(".price_color")
        #     prices = []
        #     for p in price:
        #         prices.append(p.text[1:])
            
        #     categories = soup.find_all("ul", class_="nav nav-list")
        #     book_cat = []
        #     for category in categories:
        #         book_cat = category.text.split()

            # for title in range(len(titles)):
            #     if len(titles[title]) >= 15:
            #         instock = "Instock"
            #     else:
            #         instock="Out of stock!"

        #         books_and_prices.append({"name": titles[title], "price": prices[title], "category": book_cat[title], "instock": instock})
        # for item in books_and_prices:
        #     # book_instances = Books(name=item["name"],
        #     #                       price=item["price"],
        #     #                       category=item["category"],
        #     #                       instock=item["instock"])
        #     # books_list.append(book_instances)

        #     Book.objects.create(name=item["name"],
        #                           price=item["price"],
        #                           category=item["category"],
        #                           instock=item["instock"])
        #     # books_list.append(book_instances)

        # Books.objects.bulk_create(books_list)
        books_data = Book.objects.all()
        serializer = BookSerializer(books_data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    