from django.shortcuts import render
from . models import Keys

# Create your views here.

def hello(request):
    data = {
        'data': Keys.objects.all()

    }
    return render(request, 'keys/index.html', data)

