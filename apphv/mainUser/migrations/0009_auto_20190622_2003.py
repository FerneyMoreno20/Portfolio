# Generated by Django 2.2 on 2019-06-22 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0008_auto_20190622_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='CargExpe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Empleos', verbose_name='Cargo Ocupado'),
        ),
    ]
