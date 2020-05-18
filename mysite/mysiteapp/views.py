from django.shortcuts import render
from .models import News



def blog(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога',
    }
    return render(request, 'static/blog.html', data)



def contacts(request):
    data = {
        'news': News.text,
    }
    return render(request, 'static/contacts.html', data)


def goods(request):
    data = {
        'goods_list': goods_list,
        'news': news
    }
    return render(request, 'static/goods.html', data)



