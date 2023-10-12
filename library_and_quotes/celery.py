import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_and_quotes.settings")

app = Celery("library_and_quotes")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "get_quote_3s": {
        "task": "kanye_quotes.tasks.get_quote",
        "schedule": 5.0,
    }
}

app.autodiscover_tasks()