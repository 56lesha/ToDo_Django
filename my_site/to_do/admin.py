from django.contrib import admin

from to_do.models import Task, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'priority',
                    'status', 'created', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['priority', 'status']
    ordering = ['created']

