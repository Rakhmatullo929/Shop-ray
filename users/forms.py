from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'input',
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput({
        'class': 'input',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={
        'class': 'input'
    }))
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
