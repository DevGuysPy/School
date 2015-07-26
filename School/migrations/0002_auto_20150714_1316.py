# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.AddField(
            model_name='group',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.OneToOneField(null=True, to='School.Group'),
        ),
    ]
