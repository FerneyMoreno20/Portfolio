# Generated by Django 2.2 on 2019-06-18 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainUser', '0002_experiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='CargExpe',
            field=models.ForeignKey(limit_choices_to={'EsCargo': 'SI'}, on_delete=django.db.models.deletion.CASCADE, to='parametros.Empleos', verbose_name='Cargo Ocupado'),
        ),
    ]