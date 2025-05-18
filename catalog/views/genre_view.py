from rest_framework import viewsets, decorators
from catalog.models import Genre, Book
from catalog.serializers import GenreSerializer, AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
