import os
from celery import Celery as CeleryApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshop.settings')

app = CeleryApp('myshop')
app.config_from_object('django.conf.settings',namespace='CELERY')
app.autodiscover_tasks()