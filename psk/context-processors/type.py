from products.models import Type


def all_types(request):
    return {
        'all_types': Type.objects.all(),
    }
