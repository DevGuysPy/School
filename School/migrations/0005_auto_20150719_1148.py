# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('School', '0004_auto_20150716_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='info',
            field=models.TextField(null=True, blank=True),
        ),
    ]
