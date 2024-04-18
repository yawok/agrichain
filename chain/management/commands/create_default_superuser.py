from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


USERNAME = "defaultAdmin"
EMAIL = "defaultadmin@chain.com"
PASSWORD = "defaultAdminPassword"

class Command(BaseCommand):
	""" For the purpose of creating a superuser before starting the app in a docker container. """
 
	def handle(self, *args, **options):
		if not User.objects.filter(username=USERNAME):
			User.objects.create_superuser(username=USERNAME, password=PASSWORD, email=EMAIL)
			print("Created superuser!")
		else:
			print("Superuser already exists!")