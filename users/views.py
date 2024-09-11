from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):  # наследуемся от BaseLoginView
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):  # наследуемся от BaseLogoutView
    pass


class RegisterView(CreateView):
    """Контроллер для регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Отправка письма с приветствием при регистрации"""
        new_user = form.save()  # сохраняем пользователя
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегистрировались на нашем учебном сайте, добро пожаловать!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    """Контроллер для редактирования профиля"""
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        """Избавляемся от идентификатора текущего пользователя"""
        return self.request.user

