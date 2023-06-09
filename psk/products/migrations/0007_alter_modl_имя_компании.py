# Generated by Django 4.2 on 2023-04-19 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_modl_имя_компании"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modl",
            name="Имя компании",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company",
                to="products.company",
            ),
        ),
    ]
