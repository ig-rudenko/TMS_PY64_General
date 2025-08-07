from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=32, primary_key=True, verbose_name="Тег")

    # post_set -> Связь с моделью Posts через ManyToManyField

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to="%Y/%m/%d", null=True, blank=True)

    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)

    # comment_set -> Связь с моделью Comment

    class Meta:
        db_table = "posts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        # f"/post/{self.id}"
        # Либо как правильно:
        return reverse("post-view", args=(self.id,))


class Comment(models.Model):
    text = models.CharField(max_length=4096, verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"
        ordering = ["-created_at"]
