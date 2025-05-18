from django.db import models
from core.models import BaseModel
from .books import Book
from users.models import CustomUser


class BookRating(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(choices=[(i, i)for i in range(1, 6)])
    comment = models.TextField(max_length=250)


    class Meta:
        unique_together = ['book', 'user']

    def __str__(self):
        return f'{self.user} - {self.book} (self.rating)'

