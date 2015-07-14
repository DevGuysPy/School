# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_remove_group_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.OneToOneField(to='School.Group', null=True),
        ),
    ]
