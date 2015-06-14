# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenguajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.AlterModelOptions(
            name='lenguaje',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Lenguajes'},
        ),
        migrations.RenameField(
            model_name='lenguaje',
            old_name='lenguaje',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='lenguaje',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='paradigma',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='lenguaje',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='respuestas',
            field=models.ManyToManyField(to='lenguajes.Respuesta'),
        ),
        migrations.AddField(
            model_name='tipo',
            name='lenguaje',
            field=models.ManyToManyField(to='lenguajes.Lenguaje'),
        ),
        migrations.AddField(
            model_name='paradigma',
            name='tipo',
            field=models.ManyToManyField(to='lenguajes.Tipo'),
        ),
    ]
