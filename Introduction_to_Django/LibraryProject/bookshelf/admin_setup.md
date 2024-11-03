# Django Admin Configuration for Book Model

## Steps to Register the Book Model with Admin
1. In `bookshelf/admin.py`, import the `Book` model:
   ```python
   from django.contrib import admin
   from .models import Book
