from django.contrib.auth.forms import UserCreationForm

from mailing.forms import StyleFormMixin
from users.models import User


class UserForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # password1, password2 использ-ся в UserCreationForm