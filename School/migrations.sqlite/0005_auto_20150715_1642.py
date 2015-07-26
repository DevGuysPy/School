# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0004_remove_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(null=True, to='School.Lesson')),
                ('mark', models.OneToOneField(to='School.Mark')),
            ],
        ),
        migrations.RemoveField(
            model_name='student_activity',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='student_activity',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='student_activity',
            name='student',
        ),
        migrations.AlterField(
            model_name='student',
            name='activities',
            field=models.ManyToManyField(through='School.StudentActivity', to='School.Lesson', related_name='activities'),
        ),
        migrations.DeleteModel(
            name='Student_activity',
        ),
        migrations.AddField(
            model_name='studentactivity',
            name='student',
            field=models.ForeignKey(to='School.Student'),
        ),
    ]
