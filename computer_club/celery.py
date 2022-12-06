from celery import Celery

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'computer_club.settings')


celery_app = Celery('computer_club', result_expires=60)
celery_app.config_from_object('django.conf:settings')

celery_app.autodiscover_tasks()

