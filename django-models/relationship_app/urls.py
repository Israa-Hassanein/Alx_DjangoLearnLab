from django.urls import path
from . import views
from django.urls import path
from .views import list_books, LibraryDetailView  # Import both views directly as required
from django.urls import path, include

urlpatterns = [
    path('books/', views.list_books, name='list_books'),           # Function-based view for books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library
]


urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),  # Include the app's URLs
]

