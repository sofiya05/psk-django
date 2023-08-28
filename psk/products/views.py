from django.shortcuts import get_object_or_404, render

from .models import Company, Modl, Product, Type


def index(request):
    return render(request, 'products/index.html')


def Products(request, type, company, slug):
    modl = get_object_or_404(Modl, model_slug=slug)
    products = modl.products.all()

    context = {
        'model': modl,
        'products': products,
    }

    return render(request, 'products/products.html', context)


def model(request, type, company):
    company = Company.objects.get(company_name=company)
    types = Type.objects.get(type_name=type)
    tp = ''
    if type == 'lazer':
        tp = 'лазерного'
    elif type == 'plazma':
        tp = 'плазменного'
    elif type == 'welding':
        tp == 'сварочного'

    context = {
        'tp': tp,
        'type': types,
        'company': company,
        'models': Modl.objects.filter(model_type=types).filter(
            company_name=company
        ),
    }

    return render(request, 'products/models.html', context)


def company(request, type):
    input_type = Type.objects.get(type_name=type)
    context = {
        'type': input_type,
        'companys': input_type.companys.all(),
    }
    return render(request, 'products/company.html', context)
