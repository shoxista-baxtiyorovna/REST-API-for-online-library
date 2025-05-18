from rest_framework import serializers
from lending.models import BookLending


class LendingSerializer(serializers.ModelSerializer):
    current_fine = serializers.SerializerMethodField()
    class Meta:
        model = BookLending
        fields = ['id', 'book_copy', 'borrower', 'borrowed_date', 'due_date', 'returned_date', 'current_fine', 'status']

    def get_current_fine(self, obj):
        return obj.current_fine

    def validate(self, data):
        user = data['user']
        book = data['book']
        if BookLending.objects.filter(user=user, book=book, returned=False).exists():
            raise serializers.ValidationError("You haven’t returned this book yet.")
        return data