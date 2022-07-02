from django import forms


class RecordForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Имя')
    mail = forms.EmailField(max_length=20, label='Почта')
    description = forms.CharField(max_length=2000, required=True, label='Описание')

