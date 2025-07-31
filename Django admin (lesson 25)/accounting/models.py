from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Телефон",
        help_text="Телефон в формате только цифр",
    )

    class Meta:
        db_table = "users"
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователя"
