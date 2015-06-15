# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0012_auto_20150614_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lenguaje',
            name='tipo',
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='tipos',
            field=models.ManyToManyField(to='lenguajes.Tipo'),
        ),
    ]
