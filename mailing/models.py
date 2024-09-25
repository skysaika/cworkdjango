from datetime import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from clients.models import Client

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    """
    Message Model - модель сообщения
    title: заголовок сообщения
    body: текст сообщения
    recipient: клиенты
    is_published: опубликовано
    owner: автор сообщения
    """
    title = models.CharField(max_length=150, verbose_name='заголовок сообщения')
    body = models.TextField(verbose_name='текст сообщения')
    recipients = models.ManyToManyField(Client, related_name='recipients', verbose_name='получатели')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    # сообщение принадлежит текущему пользователю:
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='автор сообщения')

    # def clean(self):
    #     if self.is_published and not self.owner:
    #         raise ValidationError('Поле "автор рассылки" обязательно к заполнению.')
    def clean(self):
        if self.is_published and self.owner is None:
            raise ValidationError('Поле "автор сообщения" обязательно к заполнению.')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        permissions = [
            ('can_view_message', 'Can view message'),  # разрешение на просмотр сообщений
        ]


class Mailing(models.Model):
    """
    Mailing Model - модель рассылки
    message: связанное сообщение
    start_time: дата начала рассылки
    end_time: дата окончания рассылки
    frequency: периодичность рассылки
    status: статус рассылки
    """
    ONCE = 'once'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'

    PERIOD_CHOICES = [
        (ONCE, 'Разово'),
        (DAILY, 'Ежедневно'),
        (WEEKLY, 'Еженедельно'),
        (MONTHLY, 'Ежемесячно'),
    ]

    DRAFT = 'draft'
    CREATED = 'created'
    RUNNING = 'running'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (DRAFT, 'Черновик'),
        (CREATED, 'Создана'),
        (RUNNING, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]
    send_name = models.CharField(max_length=255, verbose_name='имя рассылки', **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='связанное сообщение')
    start_time = models.DateTimeField(verbose_name='Начало рассылки', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='Окончание рассылки', **NULLABLE)

    frequency = models.CharField(max_length=20, choices=PERIOD_CHOICES,
                                 verbose_name='периодичность', **NULLABLE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT,
                              verbose_name='статус рассылки', **NULLABLE)
    # автор рассылки
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name='автор рассылки')

    def clean(self):
        # Проверка, что дата окончания больше даты начала
        if self.end_time and self.start_time and self.end_time <= self.start_time:
            raise ValidationError("Дата окончания должна быть больше даты начала.")



    def __str__(self):
        return f'{self.message.title} - {self.start_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        permissions = [
            ('can_view_mailing', 'Can view mailing'),  # разрешение на просмотр рассылок
            ('can_send_mailing', 'Can send mailing'),  # разрешение на отправку рассылок
            ('can_disable_mailing', 'Can disable mailing'),  # разрешение на отключение рассылок
        ]


class Log(models.Model):
    """
    Log Model: модель логов рассылок
    send_time: время последней попытки
    attempt_status: статус попытки
    server_response: ответ сервера
    mailing: рассылка
    """
    SUCCESS = 'success'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (SUCCESS, 'Успешно'),
        (FAILED, 'Неуспешно'),
    ]

    send_time = models.DateTimeField(auto_now_add=True, verbose_name='время последней попытки', **NULLABLE)
    attempt_status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='статус попытки', **NULLABLE)
    server_response = models.TextField(max_length=255, verbose_name='ответ сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE, related_name='mail_logs')

    def __str__(self):
        return f'{self.mailing.message.title} - {self.send_time}'

    def clean(self):
        # Проверка статуса попытки
        if self.attempt_status not in dict(self.STATUS_CHOICES):
            raise ValidationError("Статус попытки должен быть 'success' или 'failed'.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('attempt_status',)
