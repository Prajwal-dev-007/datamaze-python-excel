
from celery import Celery
#home = Celery('datamaze', broker='redis://localhost:6379/0')
home = Celery('datamaze', broker='redis://red-csbjaua3esus73fqvn3g:6379')

home.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from your Django apps
home.autodiscover_tasks()
"""
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datamaze.settings')

app = Celery('datamaze')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
"""