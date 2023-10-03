from rest_framework import serializers
from .models import Quote

class QuoteSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"