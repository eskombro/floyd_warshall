python manage.py migrate
./manage.py shell -c "from django.contrib.auth.models import User;
u = User.objects.filter(username='admin');
if len(u) == 0:
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
gunicorn main_project.wsgi -b 0.0.0.0:8000
