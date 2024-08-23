from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import User


class LoginView(BaseLoginView):  # наследуемся от BaseLoginView
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):  # наследуемся от BaseLogoutView
    pass


class RegisterView(CreateView):
    """Контроллер для регистрации"""
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
