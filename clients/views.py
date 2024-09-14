from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


# Create your views here.
class ClientListView(ListView):
    """Просмотр списка клиентов"""
    model = Client
    template_name = 'clients/client_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientDetailView(DetailView):
    """Просмотр информации о клиенте"""
    model = Client
    template_name = 'clients/client_detail.html'
    extra_context = {
        'title': 'Информация о клиенте'
    }


class ClientCreateView(CreateView):
    """Создание клиента"""
    model = Client
    form_class = ClientForm  # форма для создания клиента
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Создание клиента'
    }
    success_url = reverse_lazy('clients:client_list')

    def form_valid(self, form):
        """Созданная запись о клиенте принадлежит текущему пользователю"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    """Редактирование клиента"""
    model = Client
    form_class = ClientForm  # форма для редактирования клиента
    template_name = 'clients/client_form.html'
    extra_context = {
        'title': 'Редактирование клиента'
    }
    success_url = reverse_lazy('clients:client_list')


class ClientDeleteView(DeleteView):
    """Удаление клиента"""
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    extra_context = {
        'title': 'Удаление клиента'
    }
    success_url = reverse_lazy('clients:client_list')


def toggle_active(request, pk):
    """Переключение активности клиента FBV"""
    client_item = get_object_or_404(Client, pk=pk)
    if client_item.is_active:
        client_item.is_active = False
    else:
        client_item.is_active = True
    client_item.save()
    return redirect(reverse('clients:client_list'))
