from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_from = CustomUserChangeForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username',]

admin.site.register(CustomUser, CustomUserAdmin)