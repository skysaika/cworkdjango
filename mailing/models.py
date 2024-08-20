from datetime import datetime
from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Message(models.Model):
    """
    Message Model - модель сообщения
    title: тема
    body: текст рассылки
    recipient: клиенты
    is_published: опубликована
    owner: автор рассылки
    """
    title = models.CharField(max_length=255, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')
    # recipient = models.ManyToManyField(Client, related_name='clients', verbose_name='клиенты')
    # is_published = models.BooleanField(default=False, verbose_name='опубликована')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """
    Mailing Model - модель рассылки
    message: название рассылки
    start: дата начала рассылки
    finish: дата окончания рассылки
    period: периодичность рассылки
    status: статус рассылки
    """
    ONCE = 'разовая'
    DAILY = 'ежедневная'
    WEEKLY = 'еженедельная'
    MONTHLY = 'ежемесячная'

    PERIODICITY = (
        (ONCE, 'разовая'),
        (DAILY, 'ежедневная'),
        (WEEKLY, 'еженедельная'),
        (MONTHLY, 'ежемесячная'),
    )

    CREATED = 'создана'
    SENT = 'отправлена'
    CANCELED = 'отменена'

    STATUS_CHOICES = (
        (CREATED, 'создана'),
        (SENT, 'отправлена'),
        (CANCELED, 'отменена'),
    )

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='название рассылки')
    start = models.DateTimeField(verbose_name='дата начала рассылки', **NULLABLE)
    finish = models.DateTimeField(verbose_name='дата окончания рассылки', **NULLABLE)
    period = models.CharField(max_length=255, choices=PERIODICITY, verbose_name='периодичность', **NULLABLE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=CREATED,
                              verbose_name='статус рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


# class Logs(models.Model):
#     """
#     Logs Model - логи рассылок
#     mailing: рассылка
#     client: клиент
#     status: статус рассылки
#     """
#     DELIVERED = 'delivered'
#     NOT_DELIVERED = 'not_delivered'
#
#     STATUS = (
#
#     )
#     mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
#     send_time = models.DateTimeField()