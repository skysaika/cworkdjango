from django.db import models


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
