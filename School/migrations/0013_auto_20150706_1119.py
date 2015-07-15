# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0012_lesson_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='info',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='student',
            name='mark',
            field=models.ForeignKey(to='School.Mark', default=0),
            preserve_default=False,
        ),
    ]
