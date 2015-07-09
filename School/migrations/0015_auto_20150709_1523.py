# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0014_remove_student_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='mark',
            field=models.ForeignKey(default=0, to='School.Mark'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ManyToManyField(to='School.Student'),
        ),
    ]
