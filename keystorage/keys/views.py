from django.shortcuts import render,redirect
from . models import Keys
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

# def hello(request):
#     data = {
#         'data': Keys.objects.all()
#     }
#     return render(request, 'keys/index.html', data)

def index(request):
    data = {
           'data': Keys.objects.all()
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

