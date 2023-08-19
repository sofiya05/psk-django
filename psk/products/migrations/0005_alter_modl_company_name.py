# Generated by Django 4.2 on 2023-04-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_modl_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modl",
            name="company_name",
            field=models.SlugField(
                choices=[("ht", "Hypertherm"), ("ct", "Centricut")],
                max_length=200,
                null=True,
                verbose_name="Имя компании",
            ),
        ),
    ]