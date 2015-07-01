# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0009_auto_20150630_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='discipline',
            field=models.ForeignKey(to='School.Discipline'),
        ),
    ]
