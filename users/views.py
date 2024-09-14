import os
import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView, TemplateView, View

from users.forms import UserRegisterForm, UserForm

User = get_user_model()


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        new_user = form.save(commit=False) # новый пользователь
        new_user.is_active = False  # не активен
        new_user.save()  # сохраняем
        token = default_token_generator.make_token(new_user)
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))
        activation_url = reverse_lazy('users:email_confirmation', kwargs={'uidb64': uid, 'token': token})
        # Отправляем письмо с подтверждением
        current_site = get_current_site(self.request)
        send_mail(
            'Подтверждение регистрации',
            f'Перейдите по ссылке: https://{current_site}{activation_url}',
            settings.EMAIL_HOST_USER,
            [new_user.email],
            fail_silently=False,
        )
        return redirect('users:email_confirmation_sent')

        # send_mail(
        #     subject='Поздравляем с регистрацией!',
        #     message='Вы успешно зарегистрировались на аншей платформе.',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[new_user.email],
        #     fail_silently=False
        # )
        # return super().form_valid(form)


class UserConfirmEmailView(View):
    """Подтверждение почты пользователя"""
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirm_failed')


class EmailConfirmSentView(TemplateView):
    """Контроллер для отправки письма с подтверждением"""
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class EmailConfirmedView(TemplateView):
    """Контроллер успешного подтверждения почты"""
    template_name = 'users/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электронная почта подтверждена'
        return context


class EmailConfirmFailedView(TemplateView):
    """Контроллер неподтвержденной почты"""
    template_name = 'users/email_confirm_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Электронная почта не подтверждена'
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования профиля"""
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        """Избавляемся от идентификатора текущего пользователя"""
        return self.request.user

