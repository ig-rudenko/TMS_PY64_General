import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def common_task(var1: str, var2: str):
    print("Hello from celery", var1, var2)
    return f"{var1}, {var2}".upper()
