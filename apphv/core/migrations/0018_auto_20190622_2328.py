# Generated by Django 2.2.2 on 2019-06-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190622_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Solicitud', 'Solicitud'), ('Petición', 'Petición'), ('Reclamo', 'Reclamo'), ('Queja', 'Queja'), ('Felicitación', 'Felicitación')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]