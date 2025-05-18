from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


urlpatterns = [
    path('auth/register/', views.UserRegistrationView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('me', views.CurrentUserView.as_view(), name='logout'),
]