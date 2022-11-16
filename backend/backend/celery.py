import os
import sys
import uuid

from celery import Celery
from celery.schedules import crontab

from django.db import transaction
from django.conf import settings


CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CURRENT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

#  celery -A backend worker --loglevel=info -P gevent --concurrency 1 -E
app = Celery("backend")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
