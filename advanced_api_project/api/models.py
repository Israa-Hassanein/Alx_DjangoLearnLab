# The Author model represents authors in the database.
# Each author has a name and is linked to multiple books.

# The Book model represents books with their title, publication year,
# and a foreign key to the Author model.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
