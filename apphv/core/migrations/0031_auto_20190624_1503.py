# Generated by Django 2.2.2 on 2019-06-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190624_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Felicitación', 'Felicitación'), ('Queja', 'Queja'), ('Petición', 'Petición'), ('Solicitud', 'Solicitud'), ('Reclamo', 'Reclamo')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
