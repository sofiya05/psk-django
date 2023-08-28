from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from .models import Company, Modl, Product, Type


class ValidateForm(forms.ModelForm):
    model = Modl

    def clean(self):
        try:
            cleaned_data = super().clean()
            get_type = cleaned_data.get('model_type')
            get_company = cleaned_data.get('company_name')
            if get_type not in get_company.available_types.all():
                raise ValidationError(
                    'У этой организации не установлен данный тип!'
                )
            return cleaned_data
        except:
            raise ValidationError('Проверьте правильноть введенных данных!')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'article',
        'name',
        'modl',
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


class ModlAdmin(admin.ModelAdmin):
    form = ValidateForm
    list_display = (
        'model_name',
        'model_type',
        'company_name',
        'show_in_psk',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Company)
admin.site.register(Modl, ModlAdmin)
admin.site.register(Type)
