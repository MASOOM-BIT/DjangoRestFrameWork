from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField(max_length=5)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)