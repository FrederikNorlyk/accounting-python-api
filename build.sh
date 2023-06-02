#!/usr/bin/env bash
# exit on error
set -o errexit

echo poetry --version
poetry install

python manage.py collectstatic --no-input
python manage.py migrate