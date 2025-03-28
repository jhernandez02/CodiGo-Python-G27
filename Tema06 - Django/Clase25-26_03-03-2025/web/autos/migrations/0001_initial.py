# Generated by Django 5.1.6 on 2025-03-04 00:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='autos.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6)),
                ('anio', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=25)),
                ('transmision', models.CharField(choices=[('A', 'Automático'), ('M', 'Mecánico')], max_length=15)),
                ('combustible', models.CharField(choices=[('P', 'GLP'), ('V', 'GNV'), ('G', 'Gasolina'), ('D', 'Diesel'), ('E', 'Electricidad')], max_length=15)),
                ('precio', models.FloatField(default=0.0)),
                ('portada', models.CharField(choices=[('0', 'No'), ('1', 'Sí')], default='0', max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='autos.categoria')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='autos.modelo')),
            ],
        ),
    ]
