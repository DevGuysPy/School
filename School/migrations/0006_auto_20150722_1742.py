# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0005_auto_20150719_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(related_name='members', to='School.Group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='discipline',
            field=models.ForeignKey(to='School.Discipline', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
