from django.db import models

TYPES = [
    ('ls', 'Лазер'),
    ('pl', 'Плазма'),
    ('wd', 'Сварка'),
]


class Company(models.Model):
    company_name = models.CharField('Имя компании', max_length=200)

    class Meta:
        verbose_name = 'Компании'

    def __str__(self) -> str:
        return self.company_name


class Modl(models.Model):
    model_name = models.CharField('Имя модели', max_length=500)
    model_type = models.CharField(
        'Тип',
        max_length=10,
        choices=TYPES,
        default='ls',
        help_text='На какой странице будет отображаться модель',
    )
    company_name = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        name='Имя компании',
        related_name='models',
    )
    model_slug = models.SlugField(
        'Ссылка на модель',
        blank=True,
        unique=True,
        help_text='Ссылка, по которой будут доступны расходники к модели (можно оставить пустым)',
    )
    show_in_psk = models.BooleanField(
        'Показать на сайте plazmapsk',
        default=False,
        help_text='Настройка отображения на сайте',
    )

    class Meta:
        verbose_name = 'Модели'

    def __str__(self) -> str:
        return self.model_name

    def save(self, *args, **kwargs):
        if not self.model_slug:
            for char in self.model_name:
                if char == ' ':
                    char = '_'
                self.model_slug += char
        super().save(*args, **kwargs)


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
        default=0,
        related_name='models',
    )
    img = models.ImageField(
        'Изображение',
        upload_to='products/',
        null=True,
        help_text='Изображение расходника',
    )

    class Meta:
        verbose_name = 'Продукты'

    def __str__(self) -> str:
        return self.name
