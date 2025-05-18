from rest_framework import viewsets
from lending.models import BookLending
from lending.serializers import LendingSerializer
from core.permissions import IsAdminOrOperator


class LendingViewSet(viewsets.ModelViewSet):
    queryset = BookLending.objects.all()
    serializer_class = LendingSerializer
    permission_classes = [IsAdminOrOperator]