# Generated by Django 4.2 on 2023-04-20 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_alter_modl_company_name"),
    ]

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
        migrations.RemoveField(
            model_name="modl",
            name="company_name",
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_name",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="modl",
            name="model_type",
            field=models.CharField(
                choices=[("ls", "Лазер"), ("pl", "Плазма"), ("wd", "Сварка")],
                default="ls",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="modl",
            name="Имя компании",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company",
                to="products.company",
            ),
        ),
    ]
