from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from .forms import MessageForm, MailingForm
from .models import Message, Mailing


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


class MessageDeleteView(DeleteView):
    """Удаление сообщения"""
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    extra_context = {
        'title': 'Удаление сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')


class MailingListView(ListView):
    """Список рассылок"""
    model = Mailing
    template_name = 'mailing/mailing_list.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        return Mailing.objects.all()


# class MailingDetailView(DetailView):
#     """Просмотр рассылки"""
#     model = Mailing
#     template_name = 'mailing/mailing_detail.html'
#     context_object_name = 'object_list'
#     extra_context = {
#         'title': 'Просмотр рассылки'
#     }


class MailingCreateView(CreateView):
    """Создание рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    form_class = MailingForm
    extra_context = {
        'title': 'Создание рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')

