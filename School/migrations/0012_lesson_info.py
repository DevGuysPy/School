# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0011_auto_20150705_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='info',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
