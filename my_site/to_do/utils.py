from to_do.models import Category

menu = [{'title': 'Tasks', 'url_name': 'show_tasks'},
        {'title': 'Add Task', 'url_name': 'add_task'},
        {'title': 'Add Category', 'url_name': 'add_category'},
        ]


class DataMixin:
    paginate_by = 10
    def get_user_context(self, **kwargs):
        context = kwargs
        cur_user = self.request.user
        context['categories'] = Category.objects.filter(user=cur_user.id)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(2)
        context['menu'] = user_menu
        return context



