# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0018_auto_20150709_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='mark',
        ),
        migrations.AddField(
            model_name='mark',
            name='lesson',
            field=models.ForeignKey(default=0, to='School.Lesson'),
            preserve_default=False,
        ),
    ]
