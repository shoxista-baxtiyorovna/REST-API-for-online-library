from rest_framework import viewsets, decorators
from catalog.models import Genre, Book
from catalog.serializers import GenreSerializer, AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


    # @action(detail=True, methods=['get'], url_path='books', pagination_class=GenreBookPagination)
    # def books(self, request, pk=None):
    #     books = Book.objects.filter(genre__id=pk)
    #     page = self.paginate_queryset(books)
    #     serializer = AuthorBookSerializer(page, many=True) if page is not None else AuthorBookSerializer(books, many=True)
    #     return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)