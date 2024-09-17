from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


# Create your views here.
class ClientListView(LoginRequiredMixin, ListView):
    """Просмотр списка клиентов"""
    model = Client
    template_name = 'clients/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавление is_owner
        for client in context['object_list']:
            client.is_owner = client.owner == self.request.user
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Просмотр информации о клиенте"""
    model = Client
    template_name = 'clients/client_detail.html'
    extra_context = {
        'title': 'Информация о клиенте'
    }


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание клиента"""
    model = Client
    form_class = ClientForm  # форма для создания клиента
    permission_required = 'clients.add_client'
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Создание клиента'
    }
    success_url = reverse_lazy('clients:client_list')

    def form_valid(self, form):
        """Созданная запись о клиенте принадлежит текущему пользователю"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование клиента"""
    model = Client
    form_class = ClientForm  # форма для редактирования клиента
    permission_required = 'clients.change_client'
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Редактирование клиента'
    }
    success_url = reverse_lazy('clients:client_list')

    def get_object(self, queryset=None):
        """Редактировать можно только свои записи клиентов"""
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404('Вы не можете редактировать чужие записи о клиентах')
        return self.object


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление клиента"""
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    extra_context = {
        'title': 'Удаление клиента'
    }
    success_url = reverse_lazy('clients:client_list')

    def test_func(self):
        """Только суперпользователь может удалять клиентов"""
        return self.request.user.is_superuser


@login_required
def toggle_active(request, pk):
    """Переключение активности клиента FBV"""
    client_item = get_object_or_404(Client, pk=pk)
    if client_item.is_active:
        client_item.is_active = False
    else:
        client_item.is_active = True
    client_item.save()
    return redirect(reverse('clients:client_list'))
