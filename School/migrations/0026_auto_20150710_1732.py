# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0025_mark_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], default=0),
        ),
    ]
