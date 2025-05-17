from django.db import models
from catalog.models import BookCopy
from users.models import CustomUser


class BookReservation(models.Model):
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    reserver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reserved_books')
    reserved_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.book_copy} reserved by {self.reserver}'