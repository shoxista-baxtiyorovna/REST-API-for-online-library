from rest_framework import serializers
from catalog.models import Book
from .author_serializer import AuthorSerializer
from .genre_serializer import GenreSerializer


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'isbn', 'published_date', 'description', 'page_count', 'language']