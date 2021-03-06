# Generated by Django 2.2 on 2019-06-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0012_auto_20190622_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='educacion',
            name='EstaEstu',
            field=models.CharField(default='Activo', max_length=30, verbose_name='Estado de educación'),
        ),
        migrations.AlterField(
            model_name='educacion',
            name='FechGrado',
            field=models.DateField(verbose_name='Fecha de graduación'),
        ),
        migrations.AlterField(
            model_name='educacion',
            name='Instituto',
            field=models.CharField(max_length=30, verbose_name='Inistitución o Academia'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='NiveHabil',
            field=models.CharField(default='', max_length=20, verbose_name='Nivel de Habilidad: '),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='NombHabil',
            field=models.CharField(default='', max_length=100, verbose_name='Habilidad'),
        ),
        migrations.AlterField(
            model_name='logros',
            name='FechLogr',
            field=models.DateField(verbose_name='Fecha de culminación de logro'),
        ),
        migrations.AlterField(
            model_name='logros',
            name='NombLogr',
            field=models.CharField(max_length=100, verbose_name='Logro o Distinción'),
        ),
    ]
