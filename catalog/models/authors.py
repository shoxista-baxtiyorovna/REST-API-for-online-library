from django.db import models
from core.models import BaseModel


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
