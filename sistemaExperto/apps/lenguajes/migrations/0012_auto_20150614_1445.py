# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0011_auto_20150614_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lenguaje',
            options={'ordering': ['id'], 'verbose_name_plural': 'Lenguajes'},
        ),
        migrations.AlterModelOptions(
            name='paradigma',
            options={'ordering': ['id'], 'verbose_name_plural': 'Paradigmas'},
        ),
        migrations.AlterModelOptions(
            name='tipo',
            options={'ordering': ['id'], 'verbose_name_plural': 'Tipos'},
        ),
    ]
