from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from to_do.forms import AddTaskForm, RegisterUserForm
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
        return Task.objects.filter(status='P')



# def show_tasks(request):
#     tasks = Task.objects.all()
#     categories = Category.objects.all()
#     context = {'tasks': tasks,
#                'title': 'Tasks',
#                'categories':categories}
#     return render(request, 'to_do/index.html', context=context)


class TaskDetails(DataMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'to_do/task_details.html'
    slug_url_kwarg = 'task_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


# def task_details(request, task_slug):
#     task = Task.objects.get(slug=task_slug)
#     context = {'task': task, }
#     return render(request, 'to_do/task_details.html', context=context)




class ShowCategory(DataMixin, ListView):
    model = Task
    template_name = 'to_do/index.html'
    context_object_name = 'tasks'



    def get_queryset(self):
        return Task.objects.filter(category__slug=self.kwargs['cat_slug'], status='P')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=self.kwargs['cat_slug'],
                                      title=f"Категория - {context['tasks'][0].category}"
                                      )

        return dict(list(context.items()) + list(c_def.items()))




# def show_category(request, cat_slug=None):
#     tasks = Task.objects.filter(category__slug=cat_slug)
#     categories = Category.objects.all()
#
#     context = {'tasks': tasks,
#                'categories': categories,
#                'cat_selected': cat_slug
#                }
#
#     return render(request, 'to_do/index.html', context=context)


class AddTask(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'to_do/add_task.html'
    login_url = '/admin/' #перенаправляет, если пользователь не авторизован
    raise_exception = True #

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add task')
        return dict(list(context.items()) + list(c_def.items()))



# def add_task(request):
#     if request.method == 'POST':
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect('show_tasks')
#
#     else:
#         form = AddTaskForm()
#     return render(request, 'to_do/add_task.html', {'form': form,
#                                                   'title': 'Add Task'})



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'to_do/register.html'
    success_url = '/login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


def login_user(request):
    return render(request, 'to_do/login.html')




















