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
