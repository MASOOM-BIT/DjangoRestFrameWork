from rest_framework import serializers
from nsApp.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    # If you want to allow nested creation, you can use:
    class Meta:
        model = Author
        fields = '__all__'