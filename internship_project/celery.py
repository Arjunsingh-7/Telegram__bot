from __future__ import absolute_import
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')

app = Celery('internship_project')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks inside apps
app.autodiscover_tasks()
