from django.shortcuts import render
from .models import TableAndSpace
from .serializers import TableAndSpaceSerializer
from rest_framework import viewsets

class TableAndSpaceViewSet(viewsets.ModelViewSet):
    queryset = TableAndSpace.objects.all()
    serializer_class = TableAndSpaceSerializer