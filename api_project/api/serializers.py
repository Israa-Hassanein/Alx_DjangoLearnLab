# api/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Use the Book model
        fields = ['id', 'title', 'author']  # Fields to serialize
