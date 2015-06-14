# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lenguaje', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['lenguaje'],
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='Paradigma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Paradigmas',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=200)),
                ('lenguaje', models.ManyToManyField(to='lenguajes.Lenguaje')),
                ('paradigma', models.ForeignKey(to='lenguajes.Paradigma')),
            ],
            options={
                'ordering': ['pregunta'],
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=30)),
                ('lenguaje', models.ManyToManyField(to='lenguajes.Lenguaje')),
                ('pregunta', models.ForeignKey(to='lenguajes.Pregunta')),
            ],
            options={
                'ordering': ['respuesta'],
                'verbose_name_plural': 'Respuestas',
            },
        ),
    ]
