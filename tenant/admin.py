from django.contrib import admin
from .models import Resturent,ResturentTenantAwareModel

admin.site.register(Resturent)
admin.site.register(ResturentTenantAwareModel)