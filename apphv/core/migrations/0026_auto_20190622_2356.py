# Generated by Django 2.2.2 on 2019-06-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20190622_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Queja', 'Queja'), ('Felicitación', 'Felicitación'), ('Reclamo', 'Reclamo'), ('Petición', 'Petición'), ('Solicitud', 'Solicitud')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]