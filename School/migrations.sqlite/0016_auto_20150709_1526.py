# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0015_auto_20150709_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='student',
            field=models.ManyToManyField(related_name='Marks', to='School.Student'),
        ),
    ]
