# Generated by Django 4.2 on 2023-04-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name": "Название компании",
            },
        ),
        migrations.CreateModel(
            name="Modl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_name", models.TextField()),
                (
                    "company_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Название модели",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.CharField(max_length=15, verbose_name="Артикул"),
                ),
                ("name", models.TextField(verbose_name="Имя продукта")),
                (
                    "img",
                    models.ImageField(
                        null=True,
                        upload_to="products/",
                        verbose_name="Изображение",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "modl",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.modl",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукты",
            },
        ),
    ]