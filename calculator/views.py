from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'calculator/home.html')


def sobre(requets):
    return HttpResponse('Sobre')
