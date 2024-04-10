set -o errexit


cd clan

gunicorn clan.wsgi

