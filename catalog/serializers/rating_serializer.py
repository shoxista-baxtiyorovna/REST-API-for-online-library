from rest_framework import serializers
from catalog.models.rating import BookRating


class BookRatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BookRating
        fields = ['id', 'book', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']

        def validate_rating(self, value):
            if not 1 <= value <= 5:
                raise serializers.ValidationError("Rating must be between 1 and 5.")
            return value