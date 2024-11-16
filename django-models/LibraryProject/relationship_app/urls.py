from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    # User authentication URLs using class-based views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Other URL patterns for your app, such as book listing and library details
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    
    # Book management URLs (add, edit, delete)
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URL patterns for the 'relationship_app' (if needed)
    path('books/', include('relationship_app.urls')),  # Ensure correct routing if necessary
    path('add_book/', views.add_book, name='add_book'),  # Ensure this path exists
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Ensure this path exists
]
