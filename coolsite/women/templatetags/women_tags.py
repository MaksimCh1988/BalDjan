from django import template

from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/menu.html', takes_context=True)
def show_menu(context):
    request = context['request']

    if not request.user.is_authenticated:
        menu = [{'title': 'О сайте', 'url_name': 'about'},
                {'title': 'Обратная связь', 'url_name': 'contact'},
                {'title': 'Войти', 'url_name': 'login'},
                {'title': 'Регистрация', 'url_name': 'register'}]
    else:
        menu = [{'title': 'О сайте', 'url_name': 'about'},
                {'title': 'Добавить статью', 'url_name': 'add_page'},
                {'title': 'Обратная связь', 'url_name': 'contact'},
                {'title': 'Выйти', 'url_name': 'logout'},
                {'title': request.user.username, 'url_name': 'home'}]


    return {'menu': menu}
