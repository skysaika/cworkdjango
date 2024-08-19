from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """
    Client Model - модель клиентов
    email: почта
    first_name: имя
    last_name: фамилия
    comment: Комментарий
    """
    email = models.EmailField(verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    comment = models.CharField(max_length=255, verbose_name='комментарий', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.first_name} ' \
               f'{self.last_name} ' \
               f'{self.email}'

    class Meta:
        verbose_name = 'клиент рассылки'
        verbose_name_plural = 'клиенты рассылки'
        ordering = ('email',)

