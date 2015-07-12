# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0013_auto_20150706_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mark',
        ),
    ]
