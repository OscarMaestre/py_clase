# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-21 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=11)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['apellidos', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='AlumnoCursaModulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repite_modulo', models.BooleanField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
            ],
            options={
                'verbose_name_plural': 'AlumnosCursanModulo',
            },
        ),
        migrations.CreateModel(
            name='AlumnoRealizaExamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=4, max_digits=6)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AlumnoExamen', to='alumnos.Alumno')),
            ],
            options={
                'ordering': ['alumno__apellidos'],
                'verbose_name_plural': 'AlumnosRealizanExamen',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
            ],
            options={
                'verbose_name_plural': 'Examenes',
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('codigo_junta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Modulo')),
            ],
        ),
        migrations.AddField(
            model_name='examen',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Tema'),
        ),
        migrations.AddField(
            model_name='alumnorealizaexamen',
            name='examen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Examen'),
        ),
        migrations.AddField(
            model_name='alumnocursamodulo',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Modulo'),
        ),
    ]
