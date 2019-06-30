# Generated by Django 2.2 on 2019-06-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEsCi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombEtni', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiDo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiEs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLogr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombTiLo', models.CharField(max_length=50)),
            ],
        ),
    ]
