#!/usr/bin/env bash
# exit on error
set -o errexit

# Force upgrade pip and install setuptools for Python 3.12 compatibility
pip install --upgrade pip
pip install setuptools

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
