# Generated by Django 2.2.2 on 2019-06-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0013_auto_20190622_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='CeluUsua',
            field=models.CharField(default='', max_length=20, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='DireUsua',
            field=models.CharField(default='', max_length=50, verbose_name='Dirección Postal'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='GeneUsua',
            field=models.CharField(default='', max_length=1, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='RegiUsua',
            field=models.DateField(verbose_name='Registrado el: '),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='TeleUsua',
            field=models.CharField(default='', max_length=20, verbose_name='Teléfono'),
        ),
    ]
