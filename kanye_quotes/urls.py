from django.urls import path
from .views import *

urlpatterns = [
    path("kanye/quotes", KanyeQuotes.as_view()),
]
