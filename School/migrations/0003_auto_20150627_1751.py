# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_discipline_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='seats',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='surname',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
