from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_page, name='index'),
    path('blog/', views.blog, name='blog'), #параметр name присваивает этому пути имя, которое затем можно будет указывать как путь в href="", обращаясь через url - {% url 'goods' %}
    path('contacts/', views.contacts, name='contacts'),
    path('goods/', views.goods, name='goods'),

]