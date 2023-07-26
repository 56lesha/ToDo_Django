"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from to_do.views import ShowTasks, TaskDetails, ShowCategory, AddTask, RegisterUser, login_user

urlpatterns = [
    path('', ShowTasks.as_view(), name='show_tasks'),
    path('task/<slug:task_slug>/', TaskDetails.as_view(), name='task_details'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='show_category'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('register/', RegisterUser.as_view(), name ='register_user'),
    path('login/', login_user, name='login_user'),

]
