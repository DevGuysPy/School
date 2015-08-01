# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0007_auto_20150802_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='grade',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
