# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0017_auto_20150709_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='lesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='mark',
            field=models.ForeignKey(to='School.Mark', default=0),
            preserve_default=False,
        ),
    ]
