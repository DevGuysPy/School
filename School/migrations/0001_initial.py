# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('photo', models.ImageField(null=True, blank=True, upload_to='')),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('start', models.DateTimeField()),
                ('info', models.TextField()),
                ('discipline', models.ForeignKey(to='School.Discipline')),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)], default=0)),
                ('reason', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('seats', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField(null=True)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('photo', models.ImageField(null=True, blank=True, upload_to='')),
                ('info', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lesson', models.ForeignKey(null=True, to='School.Lesson')),
                ('mark', models.OneToOneField(to='School.Mark')),
                ('student', models.ForeignKey(to='School.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField(null=True)),
                ('info', models.TextField(null=True)),
                ('photo', models.ImageField(null=True, blank=True, upload_to='')),
                ('discipline', models.ForeignKey(null=True, to='School.Discipline')),
                ('group', models.OneToOneField(blank=True, to='School.Group', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='activities',
            field=models.ManyToManyField(through='School.StudentActivity', to='School.Lesson', related_name='activities'),
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='School.Group', related_name='members'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
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
            model_name='comments',
            name='comment_teacher',
            field=models.ForeignKey(to='School.Teacher'),
        ),
    ]
