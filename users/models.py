from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None  # поле удалится
    # заменим его на email, который нужно переопределить:
    email = models.EmailField(unique=True, verbose_name='почта')  # поле уникальное
    is_active = models.BooleanField(default=False)  # Поле для подтверждения почты
    email_verify_token = models.CharField(max_length=50, **NULLABLE,
                                          verbose_name='код верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
