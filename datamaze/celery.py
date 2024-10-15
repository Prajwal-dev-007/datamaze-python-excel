from celery import Celery

home = Celery('datamaze', broker='redis://localhost:6379/0')

home.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from your Django apps
home.autodiscover_tasks()
