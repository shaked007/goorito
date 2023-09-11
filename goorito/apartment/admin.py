from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GooritoUser

class CustomUserAdmin(UserAdmin):
    model = GooritoUser
    # Add custom admin configuration here

admin.site.register(GooritoUser, CustomUserAdmin)