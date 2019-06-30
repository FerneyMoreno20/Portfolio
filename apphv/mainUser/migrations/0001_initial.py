# Generated by Django 2.2 on 2019-06-18 02:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametros', '0002_empleos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdUsuario', models.CharField(default='', max_length=50, verbose_name='No. Identificación')),
                ('ImagUsua', models.ImageField(upload_to='perfiles/img', verbose_name='Foto de Perfil')),
                ('PerfilPro', ckeditor.fields.RichTextField(default='Candidato...', verbose_name='Perfil Profesional')),
                ('GeneUsua', models.CharField(default='0', max_length=1, verbose_name='Género')),
                ('TeleUsua', models.CharField(default='0', max_length=20, verbose_name='Teléfono')),
                ('CeluUsua', models.CharField(default='0', max_length=20, verbose_name='Celular')),
                ('DireUsua', models.CharField(default='0', max_length=50, verbose_name='Dirección Postal')),
                ('RegiUsua', models.DateTimeField(default='0', verbose_name='Registrado el: ')),
                ('EstaUsua', models.CharField(default='Activo', max_length=50, verbose_name='Estado')),
                ('idEstaCivil', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parametros.EstaCivil', verbose_name='Estado civil')),
                ('idEtnias', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parametros.Etnia', verbose_name='Etnias')),
                ('idTipoDocu', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parametros.TipoDocu', verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
            },
        ),
    ]
