# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
    ]
