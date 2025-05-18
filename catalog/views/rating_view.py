from rest_framework import viewsets, permissions
from catalog.models.rating import BookRating
from catalog.serializers.rating_serializer import BookRatingSerializer
from rest_framework.exceptions import ValidationError


class BookRatingViewSet(viewsets.ModelViewSet):
    serializer_class = BookRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BookRating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        user = self.request.user
        if BookRating.objects.filter(book=book, user=user).exists():
            raise ValidationError("Siz bu kitobga allaqachon baho bergansiz.")
        serializer.save(user=user)
