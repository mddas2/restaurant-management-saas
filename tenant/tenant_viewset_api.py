from rest_framework import viewsets
from django.db import connection
from .models import Restaurant,RestaurantTenantAwareModel
from .tenant_serializers import RestaurantSerializer,RestaurantAwareSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = RestaurantTenantAwareModel.objects.all()
    serializer_class = RestaurantAwareSerializer