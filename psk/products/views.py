from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'products/index.html')


def plazma(request):
    return render(request, 'products/plazma.html')


def Lazer(request):
    return render(request, 'products/lazer.html')


def Welding(request):
    return render(request, 'products/welding.html')


def about(request):
    return render(request, 'main/about.html')
