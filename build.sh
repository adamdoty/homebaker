#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
poetry env use 3.10

python manage.py collectstatic --no-input
python manage.py migrate
