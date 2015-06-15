# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0013_auto_20150615_1348'),
        ('preguntados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['paradigma'], 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterModelOptions(
            name='respuesta',
            options={'ordering': ['pregunta'], 'verbose_name_plural': 'Respuestas'},
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='respuestas',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='lenguaje',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='paradigma',
            field=models.ForeignKey(default=3, to='lenguajes.Paradigma'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='lenguajes',
            field=models.ForeignKey(default=1, to='lenguajes.Tipo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(default=1, to='preguntados.Pregunta'),
            preserve_default=False,
        ),
    ]
