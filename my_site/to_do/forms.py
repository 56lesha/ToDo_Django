from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from to_do.models import Task, Category


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class RegisterUserForm(UserCreationForm, forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

