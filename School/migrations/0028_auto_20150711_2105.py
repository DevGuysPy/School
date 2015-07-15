# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0027_auto_20150710_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='lesson',
            field=models.ForeignKey(to='School.Lesson', null=True),
        ),
    ]
