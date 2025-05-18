from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=[
            ('user', 'User'),
            ('admin', 'Admin'),
            ('operator', 'Operator'),
        ],
        default='user'
    )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def str(self):
        return self.username



class UserProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    bio = models.TextField(max_length=200)
    image = models.ImageField(blank=True, null=True)

