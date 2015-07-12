# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0019_auto_20150709_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='School.Student'),
        ),
    ]
