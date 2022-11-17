#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

pip install --upgrade pip
pip install --force-reinstall -U setuptools

python manage.py collectstatic --no-input
python manage.py migrate
