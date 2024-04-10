set -o errexit


cd hello_django

gunicorn hello_django.wsgi

