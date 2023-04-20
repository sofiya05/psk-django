from django.contrib import admin

from .models import Product, Company, Modl, Types


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'name',
        'description',
    )
    search_fields = ('article', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Company)
admin.site.register(Modl)
admin.site.register(Types)
