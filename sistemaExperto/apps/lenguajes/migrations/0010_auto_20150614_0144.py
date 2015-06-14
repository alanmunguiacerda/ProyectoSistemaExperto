# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0009_remove_lenguaje_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paradigma',
            name='tipos',
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='tipo',
            field=models.ForeignKey(default=1, to='lenguajes.Tipo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo',
            name='paradigma',
            field=models.ForeignKey(default=1, to='lenguajes.Paradigma'),
            preserve_default=False,
        ),
    ]
