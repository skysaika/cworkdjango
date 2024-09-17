from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import MessageForm, MailingForm
from .models import Message, Mailing, Log


class MessageListView(LoginRequiredMixin, ListView):
    """Список сообщений"""
    model = Message
    template_name = 'mailing/message_list.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Список сообщений'
    }

    def get_queryset(self):
        return Message.objects.all()


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Просмотр сообщения"""
    model = Message
    template_name = 'mailing/message_detail.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Просмотр сообщения'
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
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


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование сообщения"""
    model = Message
    template_name = 'mailing/message_form.html'
    form_class = MessageForm
    extra_context = {
        'title': 'Редактирование сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        """Редактировать сообщение может только создатель сообщения"""
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404('Вы не можете редактировать это сообщение')
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление сообщения"""
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    extra_context = {
        'title': 'Удаление сообщения'
    }
    success_url = reverse_lazy('mailing:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    """Список рассылок"""
    model = Mailing
    template_name = 'mailing/mailing_list.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        return Mailing.objects.all()


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Просмотр рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'object_list'
    extra_context = {
        'title': 'Просмотр рассылки'
    }

    def get_object(self, queryset=None):
        """Просмотр рассылки может только создатель рассылки"""
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404('Вы не можете просматривать это рассылку')
        return self.object

    def get_context_data(self, **kwargs):
        """Добавляем логи в контекст"""
        context = super().get_context_data(**kwargs)
        context['logs'] = Log.objects.filter(mailing=self.object).order_by('-send_time')
        return context


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Создание рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    form_class = MailingForm
    extra_context = {
        'title': 'Создание рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        """Создаваемая рассылка принадлежит текущему пользователю"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_form.html'
    form_class = MailingForm
    extra_context = {
        'title': 'Редактирование рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        """Редактировать рассылку может только создатель рассылки"""
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404('Вы не можете редактировать рассылки других пользователей')
        return self.object



class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление рассылки"""
    model = Mailing
    template_name = 'mailing/mailing_confirm_delete.html'
    extra_context = {
        'title': 'Удаление рассылки'
    }
    success_url = reverse_lazy('mailing:mailing_list')

    def test_func(self):
        """Удалить рассылку может суперпользователь"""
        return self.request.user.is_superuser


# @login_required
# def toggle_publish(request, pk):
#     message = get_object_or_404(Message, pk=pk, author=request.user)
#     message.is_published = not message.is_published
#     message.save()
#     return redirect('mailing:message_detail', pk=pk)

class LogListView(LoginRequiredMixin, ListView):
    """Список логов"""
    model = Log
    template_name = 'mailing/log_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Список логов'}

    def get_queryset(self):
        return Log.objects.all()


class LogDetailView(LoginRequiredMixin, DetailView):
    """Просмотр лога"""
    model = Log
    template_name = 'mailing/log_detail.html'
    context_object_name = 'log'
    extra_context = {'title': 'Просмотр лога'}
