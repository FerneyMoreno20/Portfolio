# Generated by Django 2.2.2 on 2019-06-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190622_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Felicitación', 'Felicitación'), ('Solicitud', 'Solicitud'), ('Petición', 'Petición'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
