from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Serializer for the Book model with custom validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime().now.year
        if current_year > value:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

# Serializer for the Author model with nested BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']