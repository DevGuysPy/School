# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0005_auto_20150715_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
