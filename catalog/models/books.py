from django.db import models
from core.models import BaseModel
from .authors import Author


class Book(BaseModel):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='book')
    isbn = models.CharField(max_length=150)
    published_date = models.DateField()
    description = models.TextField(max_length=250)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title