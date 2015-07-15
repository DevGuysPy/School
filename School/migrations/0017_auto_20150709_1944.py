# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0016_auto_20150709_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='mark',
        ),
        migrations.AddField(
            model_name='mark',
            name='lesson',
            field=models.OneToOneField(to='School.Lesson', default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='mark',
            name='student',
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.OneToOneField(to='School.Student', default=0),
            preserve_default=False,
        ),
    ]
