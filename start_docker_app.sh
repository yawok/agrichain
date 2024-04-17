#!/bin/bash

python manage.py migrate 
# python manage.py collectstatic 
python manage.py create_default_superuser
gunicorn --bind 0.0.0.0:8000 agrichain.wsgi:application