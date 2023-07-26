from django.core.cache import cache

from to_do.models import Category

menu = [{'title': 'Home', 'url_name': 'show_tasks'},
        {'title': 'Add Task', 'url_name': 'add_task'}
        ]


class DataMixin:
    paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['categories'] = Category.objects.all()
        return context
