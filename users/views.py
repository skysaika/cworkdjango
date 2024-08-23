from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import render


class LoginView(BaseLoginView):  # наследуемся от BaseLoginView
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):  # наследуемся от BaseLogoutView
    pass
