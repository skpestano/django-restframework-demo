#!/usr/bin/env bash

echo "Building project packages.."
python -m pip install -r requirements.txt

echo "Migrating Database.."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py collectstatic --noinput