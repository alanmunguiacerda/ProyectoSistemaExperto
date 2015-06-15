# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntados', '0002_auto_20150615_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='lenguajes',
            new_name='lenguaje',
        ),
    ]
