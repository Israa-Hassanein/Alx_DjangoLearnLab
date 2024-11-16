from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Sets the context object name to "library" as specified
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template path
    context_object_name = 'library'  # Context name for template

    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)
        # Add the books related to the specific library
        context['books'] = Book.objects.filter(library=self.object)
        return context
