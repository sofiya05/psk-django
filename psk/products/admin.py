from django.utils.html import format_html
from django.contrib import admin

from .models import Product, Modl, Company


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'name',
        'image',
    )
    search_fields = (
        'article',
        'name',
    )
    search_help_text = 'Можно искать по артикулу и имени'

    def image(self, obj):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(
                obj.img.url
            )
        )

    image.short_description = 'Изображение'


admin.site.register(Product, ProductAdmin)
admin.site.register(Modl)
admin.site.register(Company)
