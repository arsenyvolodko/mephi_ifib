import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mephi_ifib.settings')

app = Celery('mephi_ifib')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
