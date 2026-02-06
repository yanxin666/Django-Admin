from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'demo/demo1.html', context)

def home(request):
    return render(request, 'home.html')
