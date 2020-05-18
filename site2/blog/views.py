from django.shortcuts import render
from . models import Article

# Create your views here.

# posts = [
#     {
#         'title': 'Заголовок страницы',
#         'text': 'текст страницы',
#         'author': 'Автор страницы',
#         'date': 'дата создания страницы',
#     }
# ]

about_info = [
    {
        'phone': 'телефон',
        'address': 'адресс расположения',
        'map': 'карта проезда',
    }
]


def hello(request):
    pass

def articles(request):
    data = {
        'data': Article.objects.all()
    }
    return render(request, 'blog/articles.html', data)


def about(request):
    data = {
        'data': about_info
    }
    return render(request, 'blog/about.html', data)

def index(request):
    return render(request, 'blog/index.html')