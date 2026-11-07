from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.


from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'organization',
        'role',
        'is_active',
    )

    list_filter = (
        'role',
        'organization',
        'is_active',
    )

    search_fields = (
        'username',
        'email',
    )