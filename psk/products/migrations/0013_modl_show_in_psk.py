# Generated by Django 4.2 on 2023-05-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_alter_modl_company_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="modl",
            name="show_in_psk",
            field=models.BooleanField(
                default=False,
                help_text="Настройка отображения на сайте",
                verbose_name="Показать на сайте plazmapsk",
            ),
        ),
    ]
