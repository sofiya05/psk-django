from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse


from .models import Product, Modl, Company


def index(request):
    return render(request, 'products/index.html')


def Modls(request, company):
    modl = get_object_or_404(Company, company_name=company)
    modls = modl.company.all()
    context = {'models': modls}
    return render(request, 'products/plazma.html', context)


def Lazer(request):
    return render(request, 'products/lazer.html')


def Welding(request):
    return render(request, 'products/welding.html')


def test(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products/test.html', context)
