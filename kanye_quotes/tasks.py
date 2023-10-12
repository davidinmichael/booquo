import requests
from celery import shared_task

@shared_task
def get_quote(self, request):
        url = "https://api.kanye.rest/"
        response = requests.get(url).json()
        print(response)
        return response