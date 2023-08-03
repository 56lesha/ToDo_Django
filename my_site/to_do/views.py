from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from to_do.forms import AddTaskForm, RegisterUserForm, AddCategoryForm
from to_do.models import Task, Category
from to_do.utils import DataMixin


# Create your views here.
class ShowTasks(DataMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'to_do/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Tasks')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        cur_user = self.request.user
        return Task.objects.filter(status='P', category__user=cur_user.id).select_related('category')
        # select_related необходим для того, чтобы когда мы вытягиваем из бд данные,
        # то мы сразу же и вытягиваем данные по связанному полю, чтобы постоянно не обращаться к БД.
        # это проверяется в django toolbar


class TaskDetails(DataMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'to_do/task_details.html'
    slug_url_kwarg = 'task_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))



class AddCategory(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddCategoryForm
    template_name = 'to_do/add_category.html'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add category')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowCategory(DataMixin, ListView):
    model = Task
    template_name = 'to_do/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(category__slug=self.kwargs['cat_slug'], status='P').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(cat_selected=c.slug,
                                      title=f"Категория - {c.name}"
                                      )
        return dict(list(context.items()) + list(c_def.items()))


class AddTask(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'to_do/add_task.html'
    success_url = '/'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add task')
        return dict(list(context.items()) + list(c_def.items()))


class UpdateTask(DataMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'priority', 'status']
    template_name = 'to_do/update_task.html'
    slug_url_kwarg = 'task_slug'
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Update task')
        return dict(list(context.items()) + list(c_def.items()))


def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('show_tasks')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'to_do/register.html'
    success_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # сюда попадает форма регистрации переденная через form_class
        c_def = self.get_user_context(title="Регистрация")  # сюда попадает общая часть для кода из utils
        return dict(list(context.items()) + list(c_def.items()))  # соединяем в один словарь

    def form_valid(self, form):  # вызывается, если форма валидна
        user = form.save()  # сохраняем форму
        login(self.request, user)  # логиним
        return redirect('show_tasks')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'to_do/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login_user')
