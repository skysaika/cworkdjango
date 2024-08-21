from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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


class MessageCreateView(CreateView):
    """Создание сообщения"""
    model = Message
    template_name = 'mailing/message_form.html'
    form_class = MessageForm
    extra_context = {
        'title': 'Создание сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')


