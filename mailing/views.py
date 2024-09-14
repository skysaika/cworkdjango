from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

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

    def form_valid(self, form):
        """Создаваемое сообщение принадлежит текущему пользователю"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
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


class MailingDetailView(DetailView):
    """Просмотр рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Просмотр рассылки'
    }


class MailingCreateView(CreateView):
    """Создание рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    form_class = MailingForm
    extra_context = {
        'title': 'Создание рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    """Редактирование рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    form_class = MailingForm
    extra_context = {
        'title': 'Редактирование рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    """Удаление рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_confirm_delete.html'
    extra_context = {
        'title': 'Удаление рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')


# @login_required
# def toggle_publish(request, pk):
#     message = get_object_or_404(Message, pk=pk, author=request.user)
#     message.is_published = not message.is_published
#     message.save()
#     return redirect('mailing:message_detail', pk=pk)