from django.urls import path
from .views import *

urlpatterns = [
    path("quotes/", Quotes.as_view()),
    path("authors/", AllAuthors.as_view()),
]
