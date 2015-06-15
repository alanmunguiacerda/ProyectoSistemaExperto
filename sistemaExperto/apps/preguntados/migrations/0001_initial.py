# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0012_auto_20150614_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['tipo'],
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=30)),
                ('lenguaje', models.ForeignKey(to='lenguajes.Lenguaje')),
            ],
            options={
                'ordering': ['lenguaje'],
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='respuestas',
            field=models.ManyToManyField(to='preguntados.Respuesta'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo',
            field=models.ForeignKey(to='lenguajes.Tipo'),
        ),
    ]
