# Import the management module from django
from django.core import management

# Get the list of available apps from the settings module
import settings
apps = settings.INSTALLED_APPS

# Loop through each app and call the makemigrations command
for app in apps:
    management.call_command('makemigrations', app)