# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0009_auto_20150717_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
