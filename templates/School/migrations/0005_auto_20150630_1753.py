# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0004_auto_20150630_1751'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]
