import time

from psycopg  import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  
  def handle(self, *args, **kwargs):
    self.stdout.write("Waiting for db...")
    db_up = False
    while db_up == False:
      try: 
        self.check(databases=['default'])
        db_up = True
      except (Psycopg2OpError, OperationalError) as e:
        self.stdout.write("Database unavailable, waiting for 1 second...")
        time.sleep(1)
        
    self.stdout.write(self.style.SUCCESS("Database ready"))