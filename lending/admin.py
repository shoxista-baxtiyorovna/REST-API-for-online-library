from django.contrib import admin
from .models import BookLending, BookReservation


class BookLendingAdmin(admin.ModelAdmin):
    list_display = ('book_copy', 'borrower', 'borrowed_date', 'due_date', 'returned_date', 'status')
    list_filter = ('status', 'borrowed_date', 'due_date')
    search_fields = ('book_copy__isbn', 'borrower__username', 'borrower__email')
    ordering = ('-borrowed_date',)


class BookReservationAdmin(admin.ModelAdmin):
    list_display = ('book_copy', 'reserver', 'reserved_at', 'expires_at', 'is_active')
    list_filter = ('is_active', 'reserved_at', 'expires_at')
    search_fields = ('book_copy__isbn', 'reserver__username', 'reserver__email')
    ordering = ('-reserved_at',)


admin.site.register(BookLending, BookLendingAdmin)
admin.site.register(BookReservation, BookReservationAdmin)

