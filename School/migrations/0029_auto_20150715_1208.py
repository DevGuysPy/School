# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0028_auto_20150711_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.AddField(
            model_name='group',
            name='photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.OneToOneField(to='School.Group', blank=True, null=True),
        ),
    ]
