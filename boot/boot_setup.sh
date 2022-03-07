#!/bin/bash

printf '\n[ 🛠   Making DB migrations 🛠  ...]\n'
venv/bin/python manage.py makemigrations


printf '\n[ 🛠   Migrating DB 🛠  ...]\n'
venv/bin/python manage.py migrate


printf '\nCollecting static for django_import_export...'
venv/bin/python manage.py collectstatic --noinput

printf "\n"

venv/bin/python manage.py createsuperuser_if_not_exists \
 --username=${DJANGO_SUPERUSER_USERNAME} \
 --email=${DJANGO_SUPERUSER_EMAIL} \
 --password=${DJANGO_SUPERUSER_PASSWORD}

printf "\n"

venv/bin/python -m pytest --verbosity=1 -l

printf "\n🔥 Starting Django Server ! 🔥\n"
if [[ -n $DEBUG ]]
  then
    printf 'Initializing debuging mode'
    export DEBUG_MODE='on'
fi

exec venv/bin/python manage.py runserver 0.0.0.0:8000