# https://pypi.org/project/django-tenants/
# python manage.py migrate_schemas --shared

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin): #resturent
    name = models.CharField(max_length=100)

class Domain(DomainMixin): #be aware
    pass
