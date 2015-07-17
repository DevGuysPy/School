# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0008_auto_20150716_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
