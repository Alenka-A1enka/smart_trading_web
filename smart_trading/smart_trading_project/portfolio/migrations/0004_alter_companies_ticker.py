# Generated by Django 4.2.1 on 2023-06-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='ticker',
            field=models.CharField(unique=True, verbose_name='Тикер компании'),
        ),
    ]
