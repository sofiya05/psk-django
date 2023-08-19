from django.shortcuts import render, get_object_or_404


from .models import Product, Modl


def index(request):
    return render(request, 'products/index.html')


def Products(request, slug):
    modl = get_object_or_404(Modl, model_slug=slug, show_in_psk=True)
    products = modl.products.all()

    context = {
        'modl': modl,
        'products': products,
    }

    return render(request, 'products/products.html', context)


def Test(request, type):
    models = Modl.objects.filter(model_type=type).filter(show_in_psk=True)
    context = {'models': models}

    return render(request, 'products/plazma.html', context)
