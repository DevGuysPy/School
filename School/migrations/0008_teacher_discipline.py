# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0007_auto_20150630_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='discipline',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
