from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    myheader = 'THIS IS MY CUSTOM HEADER'
    context = {
        'myheader': myheader
    }
    return render(request, 'detect/index.html', context)
