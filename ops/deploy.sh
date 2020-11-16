#!/bin/sh
python /django-backend/manage.py migrate
python /django-backend/manage.py collectstatic --noinput
gunicorn boocs.wsgi:application -w 2 -b :8000