# Generated by Django 2.2.2 on 2019-06-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190622_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Reclamo', 'Reclamo'), ('Queja', 'Queja'), ('Petición', 'Petición'), ('Solicitud', 'Solicitud'), ('Felicitación', 'Felicitación')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
