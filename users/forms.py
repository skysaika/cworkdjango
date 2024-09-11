from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # заменили 'username' на 'email'


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования профиля пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()  # спрячем поле пароля
