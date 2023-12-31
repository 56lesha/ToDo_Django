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

from .views import *

urlpatterns = [
    path('', ShowTasks.as_view(), name='show_tasks'),
    path('task/<slug:task_slug>/', TaskDetails.as_view(), name='task_details'),
    path('category/<slug:cat_slug>', ShowCategory.as_view(), name='show_category'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('delete_category/<slug:cat_slug>', DeleteCategory.as_view(), name='delete_category'),
    path('update_task/<slug:task_slug>', UpdateTask.as_view(), name='update_task'),
    path('update_category/<slug:cat_slug>', UpdateCategory.as_view(), name='update_category'),
    path('register/', RegisterUser.as_view(), name ='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout'),

]
