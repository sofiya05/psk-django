# Generated by Django 4.2 on 2023-04-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_rename_company_name_modl_имя_компании_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modl",
            name="Имя компании",
        ),
        migrations.AddField(
            model_name="modl",
            name="company_name",
            field=models.CharField(
                default="Не указано",
                max_length=500,
                verbose_name="Компания, которой принадлежит модель",
            ),
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_name",
            field=models.CharField(
                max_length=500, verbose_name="Название модели"
            ),
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_type",
            field=models.CharField(
                choices=[("ls", "Лазер"), ("pl", "Плазма"), ("wd", "Сварка")],
                default="ls",
                max_length=10,
                verbose_name="Тип модели",
            ),
        ),
        migrations.DeleteModel(
            name="Company",
        ),
    ]
