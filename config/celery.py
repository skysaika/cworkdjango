import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем экземпляр приложения Celery
app = Celery('config')

# Загружаем конфигурации из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи
app.autodiscover_tasks()

