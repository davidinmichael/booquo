from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import lxml
import bs4

class Books(APIView):

    def get(self, request):
        response = requests.get("http://books.toscrape.com/catalogue/page-2.html")
        data = response.text
        soup = bs4.BeautifulSoup(data, "lxml")

        title = soup.select("article h3")
        titles = []
        for item in title:
            titles.append(item.text)

        price = soup.select(".price_color")
        prices = []
        for p in price:
            prices.append(p.text[1:])
        
        categories = soup.find_all("ul", class_="nav nav-list")
        book_cat = []
        for category in categories:
            book_cat = category.text.split()

        books_and_prices = []

        for title in range(len(titles)):
            if len(titles[title]) >= 15:
                instock = "Instock"
            else:
                instock="Out of stock!"

            books_and_prices.append({"name": titles[title], "price": prices[title], "category": book_cat[title], "instock": instock})

        return Response({'Books': books_and_prices}, status=status.HTTP_200_OK)