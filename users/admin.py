from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

