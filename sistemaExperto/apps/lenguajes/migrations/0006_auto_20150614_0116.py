# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0005_auto_20150613_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='lenguajes',
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='tipo',
            field=models.ForeignKey(default=b'', to='lenguajes.Tipo'),
        ),
    ]
