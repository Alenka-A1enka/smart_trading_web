# Generated by Django 4.2.1 on 2023-05-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='header',
            field=models.TextField(max_length=500, verbose_name='Заголовок статьи'),
        ),
    ]
