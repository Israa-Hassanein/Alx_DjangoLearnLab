from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.permissions import IsAuthenticated


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        # Custom validation: Ensure publication year is not in the future
        if serializer.validated_data['publication_year'] > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books
    def perform_update(self, serializer):
        # Custom validation: Ensure publication year is not in the future
        if serializer.validated_data['publication_year'] > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books
