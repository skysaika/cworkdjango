from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import MessageForm
from .models import Message


class MessageListView(ListView):
    """Список сообщений"""
    model = Message
    template_name = 'mailing/message_list.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Список сообщений'
    }

    def get_queryset(self):
        return Message.objects.all()


class MessageDetailView(DetailView):
    """Просмотр сообщения"""
    model = Message
    template_name = 'mailing/message_detail.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Просмотр сообщения'
    }



class MessageCreateView(CreateView):
    """Создание сообщения"""
    model = Message
    template_name = 'mailing/message_form.html'
    form_class = MessageForm
    extra_context = {
        'title': 'Создание сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(CreateView):
    """Редактирование сообщения"""
    model = Message
    template_name = 'mailing/message_form.html'
    form_class = MessageForm
    extra_context = {
        'title': 'Редактирование сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')


