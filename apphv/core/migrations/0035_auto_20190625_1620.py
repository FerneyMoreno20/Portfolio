# Generated by Django 2.2.2 on 2019-06-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20190624_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Felicitación', 'Felicitación'), ('Petición', 'Petición'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Solicitud', 'Solicitud')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]