from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # widgets = {
        #     'ticker': {
        #         'class': 'form-control',
        #         'placeholder': 'Имя пользователя'
        #     },
        #     'company_name': {
        #         'class': 'form-control',
        #         'placeholder': 'Пароль'
        #     }
        # }