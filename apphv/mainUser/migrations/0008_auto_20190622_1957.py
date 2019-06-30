# Generated by Django 2.2 on 2019-06-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0007_auto_20190621_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='Apellido',
            field=models.CharField(default='', max_length=200, verbose_name='Apellido'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Correo',
            field=models.CharField(default='@', max_length=250, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Nombre',
            field=models.CharField(default='', max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='educacion',
            name='FechGrado',
            field=models.CharField(default='Activo', max_length=30, verbose_name='Estado de educación'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='RegiUsua',
            field=models.DateField(default='0', verbose_name='Registrado el: '),
        ),
    ]