from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, EmailConfirmSentView, UserConfirmEmailView, \
    EmailConfirmedView, EmailConfirmFailedView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='login'),  # маршрут для входа
    path('logout/', LogoutView.as_view(), name='logout'),  # маршрут для выхода
    path('register/', never_cache(RegisterView.as_view()), name='register'),  # маршрут для регистрации закеширован
    path('profile/', never_cache(UserUpdateView.as_view()), name='profile'),  # маршрут для профиля закеширован
    path('email-confirmation-sent/', EmailConfirmSentView.as_view(), name='email_confirmation_sent'),  # письмо активации отправлено
    path('email-confirmation/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='email_confirmation'),  # активация
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),  # подтверждено
    path('email-confirm-failed/', EmailConfirmFailedView.as_view(), name='email_confirm_failed'),  # неподтверждено

]
