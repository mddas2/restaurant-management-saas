from django.shortcuts import render

# Create your views here.
# Example views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.management import call_command

@api_view(['GET'])
def testing(request,slug):
    # Call makemigrations and migrate commands
    # print("migrate ongoing...")
    # call_command('makemigrations', interactive=False)
    # call_command('migrate', interactive=False)
    # print("migrate completed")
    print(request.tenant)
    return Response({'message': 'Migrations completed successfully md'})
