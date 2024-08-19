from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

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