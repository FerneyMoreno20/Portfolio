# Generated by Django 2.2 on 2019-06-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20190625_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tipom',
            field=models.CharField(choices=[('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Felicitación', 'Felicitación'), ('Petición', 'Petición'), ('Solicitud', 'Solicitud')], default='Petición', max_length=50, verbose_name='Categoría'),
        ),
    ]
