from django import forms
from .models import Book  # Replace `Book` with the correct model if applicable

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Replace `Book` with the actual model
        fields = ['title', 'author', 'published_date']  # Replace these fields with the ones relevant to your model
