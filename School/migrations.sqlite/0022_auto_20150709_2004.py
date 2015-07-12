# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0021_group_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='participants',
        ),
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ForeignKey(to='School.Student', default=0, related_name='Students'),
            preserve_default=False,
        ),
    ]
