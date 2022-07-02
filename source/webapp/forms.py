from django import forms
from webapp.models import STATUS_CHOICES


class RecordForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Имя')
    mail = forms.EmailField(max_length=20, label='Почта')
    description = forms.CharField(max_length=2000, required=True, label='Описание')
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Статус")
