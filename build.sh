set -o errexit

pip install -r requirements.txt

cd hello_django

python manage.py collectstatic --no-input
python manage.py migrate


echo "import os; from django.contrib.auth import get_user_model; User = get_user_model(); USERNAME = os.environ.get('USERNAME'); PASSWORD = os.environ.get('PASSWORD'); User.objects.filter(username=USERNAME).exists() or User.objects.create_superuser(USERNAME, '', PASSWORD)" | python manage.py shell

# python manage.py tailwind start