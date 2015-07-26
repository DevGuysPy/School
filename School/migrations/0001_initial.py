# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('member', models.IntegerField(default=0)),
                ('info', models.TextField()),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('info', models.TextField()),
                ('discipline', models.ForeignKey(to='School.Discipline')),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)])),
                ('reason', models.CharField(max_length=150)),
                ('lesson', models.ForeignKey(to='School.Lesson', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seats', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')])),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('info', models.TextField()),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('info', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('discipline', models.ForeignKey(to='School.Discipline')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(to='School.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='room',
            field=models.ForeignKey(to='School.Room'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(to='School.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(to='School.Teacher'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_teacher',
            field=models.ForeignKey(to='School.Teacher'),
        ),
    ]
