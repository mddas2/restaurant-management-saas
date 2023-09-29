from django.contrib.auth.models import Group, Permission
from django.contrib import admin

from .models import CustomUser


admin.site.register(CustomUser)
admin.site.register(Permission)