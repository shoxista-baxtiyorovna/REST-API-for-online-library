from django.db import models
from django.utils import timezone
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

    @property
    def current_fine(self):
        if self.status == 'overdue' and not self.returned_date:
            days_late = (timezone.now().date() - self.due_date).days
            return max(0, days_late * 1000)
        return 0


    def __str__(self):
        return f'{self.book_copy} {self.borrower}'