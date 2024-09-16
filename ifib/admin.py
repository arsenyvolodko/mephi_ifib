from .forms import CustomUserForm
from .models import TeamMember

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserForm
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Roles', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_superuser', )}),
    )


admin.site.register(TeamMember)
admin.site.register(User, CustomUserAdmin)
