# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0006_auto_20150716_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='School.Group', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
