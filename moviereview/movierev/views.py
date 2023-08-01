from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # httpRequest
    return HttpResponse("Страница приложения")

def cat(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def main(request):
    return HttpResponse("<h1>main page</h1>")


