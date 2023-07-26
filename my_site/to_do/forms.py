from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from to_do.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')