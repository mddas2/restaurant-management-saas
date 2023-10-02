# Example views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.management import call_command
from .models import Resturent

@api_view(['GET'])
def run_migrations(request):
    # Call makemigrations and migrate commands
    # print("migrate ongoing...")
    # call_command('makemigrations', interactive=False)
    # call_command('migrate', interactive=False)
    # print("migrate completed")
    tenant = Resturent(schema_name = "C res")
    tenant.save()
    print(request.tenant)
    return Response({'message': 'Migrations completed successfully md'})
