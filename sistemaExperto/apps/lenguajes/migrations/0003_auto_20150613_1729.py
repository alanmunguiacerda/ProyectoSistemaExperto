# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0002_auto_20150613_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paradigma',
            old_name='tipo',
            new_name='tipos',
        ),
        migrations.RenameField(
            model_name='tipo',
            old_name='lenguaje',
            new_name='lenguajes',
        ),
    ]
