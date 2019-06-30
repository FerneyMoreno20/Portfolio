# Generated by Django 2.2.2 on 2019-06-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0021_auto_20190622_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='GeneUsua',
            field=models.CharField(max_length=1, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='IdUsuario',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='No. Identificación'),
        ),
    ]