from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.utils.text import slugify

from to_do.models import Task, Category


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'category']

    def save(self, commit=True):
        instance = super().save(commit=False)  # вызывает родительский метод без сохранения его в БД
        if not instance.slug:
            instance.slug = slugify(instance.title)  # делаем слаг, преобразованием name в слаг
        instance.save()
        return instance


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
        fields = ['name']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            instance.slug = slugify(instance.name)
        instance.save()
        return instance
