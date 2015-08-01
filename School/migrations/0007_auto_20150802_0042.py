# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0006_auto_20150722_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
