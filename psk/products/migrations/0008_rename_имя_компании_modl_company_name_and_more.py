# Generated by Django 4.2 on 2023-04-19 22:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_modl_имя_компании"),
    ]

    operations = [
        migrations.RenameField(
            model_name="modl",
            old_name="Имя компании",
            new_name="company_name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Модель оборудования",
            new_name="modl",
        ),
    ]
