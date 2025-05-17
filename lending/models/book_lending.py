from django.db import models
from catalog.models import BookCopy
from users.models import CustomUser


class BookLending(models.Model):
    LENDING_STATUS = [
        ('active', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='lendings')
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='borrowed_books')
    borrowed_date = models.DateTimeField()
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=LENDING_STATUS)

    def __str__(self):
        return f'{self.book_copy} {self.borrower}'