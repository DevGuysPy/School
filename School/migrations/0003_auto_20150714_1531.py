# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0002_auto_20150714_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='group',
            field=models.OneToOneField(to='School.Group', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
    ]
