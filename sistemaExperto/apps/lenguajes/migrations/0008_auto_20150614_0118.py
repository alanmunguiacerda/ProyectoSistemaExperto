# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0007_auto_20150614_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenguaje',
            name='tipo',
            field=models.ForeignKey(to='lenguajes.Tipo'),
        ),
    ]
