from django.contrib import admin
from .models import Author, Genre, Book, BookCopy, BookRating


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'nationality')
    search_fields = ('first_name', 'last_name')
    list_filter = ('nationality',)
    ordering = ('last_name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'genre', 'isbn', 'published_date', 'page_count', 'language')
    search_fields = ('title', 'isbn', 'authors__first_name', 'authors__last_name', 'genre__name')
    list_filter = ('genre', 'authors')
    ordering = ('published_date',)

    def get_authors(self, obj):
        return ", ".join([author.first_name + " " + author.last_name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'inventory_number', 'condition', 'is_available', 'added_date')
    search_fields = ('book__title', 'inventory_number', 'condition')
    list_filter = ('condition', 'is_available', 'book__genre')
    ordering = ('added_date',)


@admin.register(BookRating)
class BookRatingAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'comment', 'created_at')
    search_fields = ('book', 'rating', 'comment')
    list_filter = ('book', 'rating')
    ordering = ('created_at',)

