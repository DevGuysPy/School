# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0020_auto_20150709_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(to='School.Student', related_name='Students'),
        ),
    ]
