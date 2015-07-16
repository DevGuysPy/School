# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0007_auto_20150716_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='discipline',
            field=models.ForeignKey(null=True, to='School.Discipline'),
        ),
    ]
