# Generated by Django 2.2.2 on 2019-06-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20190622_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Reclamo', 'Reclamo'), ('Felicitación', 'Felicitación'), ('Queja', 'Queja'), ('Solicitud', 'Solicitud'), ('Petición', 'Petición')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
