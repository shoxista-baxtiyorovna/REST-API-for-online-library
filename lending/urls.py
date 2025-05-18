from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LendingViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'lendings', LendingViewSet, basename='lendings')
router.register(r'reservation', ReservationViewSet, basename='reservation')



urlpatterns = [
    path('', include(router.urls)),
]