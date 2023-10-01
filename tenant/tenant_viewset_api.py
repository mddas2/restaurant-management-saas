from rest_framework import viewsets
from django.db import connection
from .models import Client,Domain
from .tenant_serializers import ClientSerializer,DomainSerializer

class ClientViewSet(viewsets.ModelViewSet):
    connection.set_schema_to_public()
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer