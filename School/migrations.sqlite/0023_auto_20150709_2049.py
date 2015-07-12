# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0022_auto_20150709_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='participants',
        ),
        migrations.AddField(
            model_name='mark',
            name='reason',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
