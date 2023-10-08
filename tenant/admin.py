from django.contrib import admin
from .models import Restaurant,RestaurantTenantAwareModel

admin.site.register(Restaurant)
admin.site.register(RestaurantTenantAwareModel)