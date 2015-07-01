# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0008_teacher_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='info',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='group',
            table='group',
        ),
    ]
