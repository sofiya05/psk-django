# Generated by Django 4.2 on 2023-08-19 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0015_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'type_name',
                    models.CharField(max_length=50, verbose_name='Тип'),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name='modl',
            name='model_type',
        ),
        migrations.AlterField(
            model_name='product',
            name='Модель оборудования',
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='products',
                to='products.modl',
            ),
        ),
        migrations.AddField(
            model_name='modl',
            name='Тип модели',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='types',
                to='products.types',
            ),
            preserve_default=False,
        ),
    ]