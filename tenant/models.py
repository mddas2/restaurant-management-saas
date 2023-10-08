# https://pypi.org/project/django-tenants/
# python manage.py migrate_schemas --shared

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Restaurant(TenantMixin): #Restaurant
    name = models.CharField(max_length=100)

class RestaurantTenantAwareModel(DomainMixin): #And then create a class TenantAwareModel class which other models will subclass from it,(in all models it's tenant id goes)
    pass

class RestaurantAwareModel(models.Model): #this model is used for put tenant id for all shared app.
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    class Meta:
        abstract = True