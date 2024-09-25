from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from clients.models import Client
from mailing.models import Mailing, Message
from vlog.models import VlogPost


class IndexView(LoginRequiredMixin, TemplateView):
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

        # Подсчитываем проведенные рассылки (например, статус "завершена" или "запущена")
        conducted_mailings_count = Mailing.objects.filter(status__in=['completed', 'running']).count()
        context['conducted_mailings_count'] = conducted_mailings_count

        # Последние 3 сообщения
        context['last_messages'] = Message.objects.order_by('-id')[:3]  # id увеличивается с каждым сообщением

        # Последние 3 рассылки
        context['last_mailings'] = Mailing.objects.order_by('-id')[:3]  # id увеличивается

        # Последние 3 активных клиента (созданных пользователем, например, с полем owner)
        context['last_active_clients'] = Client.objects.filter(is_active=True).order_by('-id')[:3]

        # 3 случайных поста
        context['posts'] = VlogPost.objects.order_by('-id')[:3]

        return context
