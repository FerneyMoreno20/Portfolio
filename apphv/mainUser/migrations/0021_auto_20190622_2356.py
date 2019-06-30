# Generated by Django 2.2.2 on 2019-06-22 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_empleos'),
        ('mainUser', '0020_remove_usuarios_idestacivil'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='RegiUsua',
            field=models.DateField(null=True, verbose_name='Registrado el: '),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='idEstaCivil',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.EstaCivil', verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='IdUsuario',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='No. Identificación'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='idEtnias',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Etnia', verbose_name='Etnias'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='idTipoDocu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.TipoDocu', verbose_name='Tipo de documento'),
        ),
    ]