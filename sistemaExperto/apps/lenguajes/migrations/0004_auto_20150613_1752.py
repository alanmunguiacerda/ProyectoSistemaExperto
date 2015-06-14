# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0003_auto_20150613_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='lenguajes',
            field=models.ManyToManyField(to='lenguajes.Lenguaje'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='tipos',
            field=models.ManyToManyField(to='lenguajes.Tipo'),
        ),
    ]
