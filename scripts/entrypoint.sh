#!/bin/bash

set -e

if [[ $1 == web ]]; then
  echo "Running Django migrations"
  python manage.py migrate
  echo "Starting Django Web Server"
  python manage.py runserver 0.0.0.0:8000
elif [[ $1 == worker ]]; then
  echo "Running Celery worker"
  celery -A trackbinance worker --loglevel=INFO
elif [[ $1 == beat ]]; then
  echo "Running Celery beat"
  celery -A trackbinance beat --loglevel=INFO
elif [[ $1 == test ]]; then
  echo "Running tests"
  python manage.py test
else
  echo "Unknown options: $1"
  echo "Must be either web, worker, beat or test"
fi