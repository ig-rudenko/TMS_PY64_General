import time

from celery import shared_task
from django.db.models import Sum, F
from django.db.models.functions import Length

from posts.api.filters import PostFilter
from posts.models import Post


@shared_task
def common_shared_task(var1: str, var2: str):
    time.sleep(3)
    print("Hello from celery shared_task", var1, var2)
    return f"shared_task {var1}, {var2}".upper()


@shared_task
def char_count_posts(**kwargs) -> dict:
    filter_ = PostFilter(data=kwargs, queryset=Post.objects.all())

    count = filter_.qs.annotate(
        char_count=Length("content"),
    ).aggregate(
        total_char_count=Sum(F("char_count")),
    )
    print(count)
    return dict(count)
