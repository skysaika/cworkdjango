from django import forms
from django.forms import CheckboxInput

from clients.models import Client
from .models import Message, Mailing


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):
    """Основная форма создания сообщения рассылки: тема, сообщение, список получателей"""
    recipient = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'})  # добавьте класс для управления стилем
    )

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     super().__init__(*args, **kwargs)
    #     if user.is_superuser:
    #         self.fields['recipient'].queryset = Client.objects.all()
    #     else:
    #         self.fields['recipient'].queryset = Client.objects.filter(owner=user)

    class Meta:
        model = Message
        fields = ('title', 'body', 'recipient', 'is_published')


class MailingForm(forms.ModelForm):
    """Форма для рассылки: время начала, время окончания, периодичность"""

    class Meta:
        model = Mailing
        fields = ('send_name','message', 'start_time', 'end_time', 'frequency', 'status')
        widgets = {
            'start_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'placeholder': 'Введите дату и время начала'
            }),
            'end_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'placeholder': 'Введите дату и время окончания'
            }),
        }
