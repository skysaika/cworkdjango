import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class VlogPost(models.Model):
    """Модель поста"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    # связь с текущим юзером
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            # если значение slug не задано, создаем его на основе заголовка статьи и случайного UUID
            self.slug = slugify(self.title) + '-' + str(uuid.uuid4().hex[:6])
            # проверяем, что значение slug уникально
            while VlogPost.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + '-' + str(uuid.uuid4().hex[:6])
        super(VlogPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created']
        permissions = [
            ('can_publish', 'Может опубликовать'),
        ]
