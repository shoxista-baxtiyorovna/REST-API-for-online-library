from rest_framework import serializers
from catalog.models import BookCopy
from .book_serializer import BookSerializer


class BookCopySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookCopy
        fields = ['id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date']

    def validate(self, data):
        if data['book'].available_copies <= 0:
            raise serializers.ValidationError("This book is currently not available in any copies.")
        return data