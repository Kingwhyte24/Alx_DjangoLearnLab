from django.db import models

# Create your models here.

# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=250)

# Book model representing a one-to-many relationship with Author
class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, )
