from rest_framework import serializers
from lending.models import BookLending


class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = ['id', 'book_copy', 'borrower', 'borrowed_date', 'due_date', 'returned_date', 'status']
