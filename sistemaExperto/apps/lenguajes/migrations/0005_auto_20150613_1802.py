# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0004_auto_20150613_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='respuestas',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='lenguajes',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='tipos',
        ),
        migrations.AddField(
            model_name='paradigma',
            name='pregunta',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='tipo',
            name='pregunta',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
    ]
