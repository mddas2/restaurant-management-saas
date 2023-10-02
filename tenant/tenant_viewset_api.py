from rest_framework import viewsets
from django.db import connection
from .models import Resturent,ResturentTenantAwareModel
from .tenant_serializers import ResturentSerializer,ResturentAwareSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Resturent.objects.all()
    serializer_class = ResturentSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = ResturentTenantAwareModel.objects.all()
    serializer_class = ResturentAwareSerializer