# coding=utf-8
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send_email_every_five_minute': {
#         'task': 'main.tasks.send_mass_mails',
#         'schedule': crontab(5),
#     },
#     'get_log_every_five_minute': {
#         'task': 'main.tasks.get_logs',
#         'schedule': crontab(5),
#     }
# }

if __name__ == "__main__":
    app.start()
