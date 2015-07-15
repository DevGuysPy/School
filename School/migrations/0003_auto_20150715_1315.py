# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0002_auto_20150715_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(null=True, to='School.Lesson')),
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
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_activity',
            name='mark',
            field=models.OneToOneField(to='School.Mark'),
        ),
        migrations.AddField(
            model_name='student_activity',
            name='student',
            field=models.ForeignKey(to='School.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='activities',
            field=models.ManyToManyField(related_name='activities', through='School.Student_activity', to='School.Lesson'),
        ),
    ]
