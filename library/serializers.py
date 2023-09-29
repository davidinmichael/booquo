from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"