# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0010_auto_20150614_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paradigma',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='tipo',
            name='pregunta',
        ),
    ]
