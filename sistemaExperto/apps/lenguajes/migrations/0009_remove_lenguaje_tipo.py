# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0008_auto_20150614_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lenguaje',
            name='tipo',
        ),
    ]
