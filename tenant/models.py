# https://pypi.org/project/django-tenants/
# python manage.py migrate_schemas --shared

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Resturent(TenantMixin): #resturent
    name = models.CharField(max_length=100)

class ResturentTenantAwareModel(DomainMixin): #And then create a class TenantAwareModel class which other models will subclass from it,(in all models it's tenant id goes)
    pass

class ResturentAwareModel(models.Model):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
