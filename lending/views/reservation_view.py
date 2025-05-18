from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets
from lending.models import BookReservation
from lending.serializers import ReservationSerializer
from core.permissions import IsUser


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        return BookReservation.objects.filter(reserver=self.request.user)

    def perform_create(self, serializer):
        self.expire_old_reservations()
        expires_at = timezone.now() + timedelta(days=1)
        serializer.save(reserver=self.request.user, expires_at=expires_at)

    def expire_old_reservations(self):
        now = timezone.now()
        expired_reservations = BookReservation.objects.filter(
            is_active=True,
            expires_at__lt=now
        )
        expired_reservations.update(is_active=False)
