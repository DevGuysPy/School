# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0023_auto_20150709_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='number',
        ),
    ]
