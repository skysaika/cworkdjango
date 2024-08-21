from django.shortcuts import render
from django.views.generic import TemplateView

from clients.models import Client
from mailing.models import Mailing


class IndexView(TemplateView):
    """Представление главной страницы."""
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
    }

    def get_context_data(self, **kwargs):
        """Добавляем количество уникальных и активных клиентов в контекст."""
        context = super().get_context_data(**kwargs)

        # Подсчитываем уникальных клиентов
        unique_clients_count = Client.objects.values('email').distinct().count()
        context['unique_clients_count'] = unique_clients_count

        # Подсчитываем активных клиентов
        active_clients_count = Client.objects.filter(is_active=True).count()
        context['active_clients_count'] = active_clients_count

        # Подсчитываем общее количество рассылок
        total_mailings_count = Mailing.objects.count()
        context['total_mailings_count'] = total_mailings_count

        return context
