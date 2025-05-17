from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)
