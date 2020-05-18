from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),
]
