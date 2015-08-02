# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0008_teacher_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='grade',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(max_length=50),
        ),
    ]
