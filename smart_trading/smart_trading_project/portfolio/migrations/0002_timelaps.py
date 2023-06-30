# Generated by Django 4.2.1 on 2023-06-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeLaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_value', models.CharField(verbose_name='Временной промежуток')),
            ],
            options={
                'verbose_name': 'Временной промежуток',
                'verbose_name_plural': 'Временные промежутки',
            },
        ),
    ]
