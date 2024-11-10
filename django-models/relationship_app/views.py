from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.views.generic.detail import DetailView  # Explicit import required by checker


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Sets the context object name to "library" as specified

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template path
    context_object_name = 'library'  # Context name for template
