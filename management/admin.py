from django.contrib import admin

from .models import FoodCategory, MenuCategory, FoodItem


admin.site.register(FoodCategory)
admin.site.register(MenuCategory)
admin.site.register(FoodItem)