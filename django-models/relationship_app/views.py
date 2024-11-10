from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Ensures the template file is explicitly set
    context_object_name = 'library'  # Sets the context object name to "library" as specified
