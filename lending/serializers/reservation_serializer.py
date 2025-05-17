from rest_framework import serializers
from lending.models import BookLending


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = ['id', 'book_copy', 'reserver', 'reserved_at', 'expires_at', 'is_active']


