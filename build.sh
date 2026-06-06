#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --fake blog 0004_auto_20260606_1439
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input