from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ['Маршруты', 'Отели и гостиницы', 'Еда']
def mainpage(request):
    smol = Smolensk.objects.all()
    return render(request, 'diplomapp/mainpage.html', {'smolinfo': smol, 'menu': menu, 'title': "Главная страница"})

def routes_1(request):
    return render(request, 'diplomapp/routes-1.html', {'menu': menu, 'title': "Усадьба Глинки"})


def routes(request):
    return render(request, 'diplomapp/routes.html', {'menu': menu, 'title': "Маршруты"})


def routes_2(request):
    return render(request, 'diplomapp/routes-2.html', {'menu': menu, 'title': "Смоленск"})
def hotels(request):
    return render(request, 'diplomapp/hotels.html', {'menu': menu, 'title': "Отели и гостиницы"})

def food(request):
    return render(request, 'diplomapp/food.html', {'menu': menu, 'title': "Еда"})
