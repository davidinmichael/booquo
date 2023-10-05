from django.urls import path
from .views import *

urlpatterns = [
    path("books/", Books.as_view()),
    path("books/<str:id>/", SingleBook.as_view()),
]
