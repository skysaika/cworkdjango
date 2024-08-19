from django import forms
from django.forms import CheckboxInput

from clients.models import Client


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма создания клиента"""
    class Meta:
        model = Client
        # указываю только один из 3 способов заполнения поля
        # fields = '__all__'
        fields = ('email', 'first_name', 'last_name', 'comment')
        # exclude = ('email',)
