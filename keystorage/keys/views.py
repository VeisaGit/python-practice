from django.shortcuts import render, redirect
from .models import Keys
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .filters import OrderFilter

# Create your views here.

# def hello(request):
#     data = {
#         'data': Keys.objects.all()
#     }

def index(request):

    orders = Keys.objects.all()

    myFilter = OrderFilter(request.GET, queryset=orders)


    data = {
        'data': myFilter.qs,
        # 'key': Keys.key,
        # 'key_user': Keys.key_user,
        # 'key_kcv': Keys.key_kcv,
        # 'key_type': Keys.key_type,
        'myFilter': myFilter,
    }


    return render(request, 'keys/index.html', data)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#
#     else:
#         form = UserCreationForm()
#
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)


