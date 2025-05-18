from rest_framework import serializers
from lending.models import BookReservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReservation
        fields = ['id', 'book_copy', 'reserver', 'reserved_at', 'expires_at', 'is_active']

    def validate(self, data):
        if BookReservation.objects.filter(user=data['user'], book=data['book'], active=True).exists():
            raise serializers.ValidationError("You have already reserved this book.")
        return data

