# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0006_auto_20150630_1829'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]
