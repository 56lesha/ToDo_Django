from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug':self.slug},)



class Task(models.Model):
    class TaskPriority(models.TextChoices):
        HIGH = 'H', 'High'
        MEDIUM = 'M', 'Medium'
        LOW = 'L', 'Low'


    class TaskStatus(models.TextChoices):
        IN_PROGRESS = 'P', 'In Progress'
        FINISHED = 'F', 'Finished'


    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=1,
                                choices=TaskPriority.choices,
                                default=TaskPriority.MEDIUM)
    status = models.CharField(max_length=1,
                              choices=TaskStatus.choices,
                              default=TaskStatus.IN_PROGRESS)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')

    def get_absolute_url(self):
        return reverse('task_details', kwargs={'task_slug': self.slug}) #reverse - получает ссылку по имени на определённое представление, передавая аргументы

    def __str__(self):
        return self.title


