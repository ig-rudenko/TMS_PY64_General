from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to="%Y/%m/%d", null=True, blank=True)

    class Meta:
        db_table = 'posts'
        ordering = ["-created_at"]


class Comment(models.Model):
    text = models.CharField(max_length=4096, verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'
        ordering = ["-created_at"]
