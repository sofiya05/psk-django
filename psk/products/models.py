from django.db import models


class Types(models.Model):
    type_name = models.CharField('Тип', max_length=20)

    class Meta:
        verbose_name = 'Типы'

    def __str__(self) -> str:
        return self.type_name


class Company(models.Model):
    company_name = models.TextField('Имя компании', unique=True)
    company_type = models.ForeignKey(
        Types,
        on_delete=models.CASCADE,
        name='Тип',
        related_name='company_types',
        default=0,
    )

    class Meta:
        verbose_name = 'Компании'

    def __str__(self) -> str:
        return self.company_name


class Modl(models.Model):
    model_name = models.CharField('Имя модели', max_length=500)
    model_type = models.ForeignKey(
        Types,
        on_delete=models.CASCADE,
        name='Тип модели',
        related_name='modl_types',
        default=0,
    )
    company_name = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        name='Имя компании',
        related_name='company',
        default=0,
    )

    class Meta:
        verbose_name = 'Модели'

    def __str__(self) -> str:
        return self.model_name


class Product(models.Model):
    article = models.CharField('Артикул', max_length=15)
    name = models.CharField('Имя продукта', max_length=200)
    description = models.TextField(
        'Описание',
    )
    modl = models.ForeignKey(
        Modl,
        on_delete=models.CASCADE,
        name='Модель оборудования',
        null=True,
        related_name='models',
    )
    img = models.ImageField('Изображение', upload_to='products/', null=True)

    class Meta:
        verbose_name = 'Продукты'

    def __str__(self) -> str:
        return self.name
