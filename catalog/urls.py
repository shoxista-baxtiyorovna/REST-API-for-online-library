from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
        GenreViewSet,
        AuthorViewSet,
        BookViewSet,
        BookCopyViewSet,
        BookRatingViewSet
)

router = DefaultRouter()
router.register(r'genres', BookRatingViewSet, basename='genres')
router.register(r'authors', BookRatingViewSet, basename='authors')
router.register(r'books', BookRatingViewSet, basename='books')
router.register(r'bookcopies', BookRatingViewSet, basename='bookcopies')
router.register(r'ratings', BookRatingViewSet, basename='ratings')


urlpatterns = [
    path('', include(router.urls)),
]