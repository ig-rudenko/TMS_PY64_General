import binascii
import os

from django.utils.translation import gettext_lazy as _

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


class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.ForeignKey(User, related_name="tokens", on_delete=models.CASCADE, verbose_name=_("User"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    expires = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "api_tokens"
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
