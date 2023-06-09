# Generated by Django 4.2 on 2023-04-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0015_types_remove_modl_model_type_alter_modl_имя_компании_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name": "Компании"},
        ),
        migrations.AlterModelOptions(
            name="modl",
            options={"verbose_name": "Модели"},
        ),
        migrations.AlterModelOptions(
            name="types",
            options={"verbose_name": "Типы"},
        ),
        migrations.AlterField(
            model_name="company",
            name="company_name",
            field=models.TextField(unique=True, verbose_name="Имя компании"),
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_name",
            field=models.CharField(max_length=500, verbose_name="Имя модели"),
        ),
        migrations.AlterField(
            model_name="types",
            name="type_name",
            field=models.CharField(max_length=20, verbose_name="Тип"),
        ),
    ]
