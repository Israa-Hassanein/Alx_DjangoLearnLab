from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter  # Correctly importing these filters
from django_filters import rest_framework as filters  # Importing DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Applying filters properly
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]  # Ensure correct filters are included
    filterset_fields = ['title', 'author', 'publication_year']  # Fields that can be filtered
    search_fields = ['title', 'author']  # Fields that can be searched
    ordering_fields = ['title', 'publication_year']  # Fields that can be ordered

    # ListView supports filtering by title, author, and publication year
    # Search is enabled on the title and author fields
    # Ordering is enabled by title and publication year, including descending order


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
