# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_auto_20150715_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson', models.ForeignKey(to='School.Lesson', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mark',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='studentactivity',
            name='mark',
            field=models.OneToOneField(to='School.Mark'),
        ),
        migrations.AddField(
            model_name='studentactivity',
            name='student',
            field=models.ForeignKey(to='School.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='activities',
            field=models.ManyToManyField(related_name='activities', through='School.StudentActivity', to='School.Lesson'),
        ),
    ]
