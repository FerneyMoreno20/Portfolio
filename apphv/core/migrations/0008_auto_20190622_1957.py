# Generated by Django 2.2 on 2019-06-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190622_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Felicitación', 'Felicitación'), ('Petición', 'Petición'), ('Reclamo', 'Reclamo'), ('Solicitud', 'Solicitud'), ('Queja', 'Queja')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
