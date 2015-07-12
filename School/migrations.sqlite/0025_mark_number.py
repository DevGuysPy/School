# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0024_remove_mark_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
