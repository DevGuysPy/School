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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('comment_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='', blank=True)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('info', models.TextField()),
                ('discipline', models.ForeignKey(to='School.Discipline')),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)], default=0)),
                ('reason', models.CharField(max_length=150)),
                ('lesson', models.ForeignKey(null=True, to='School.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('seats', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('photo', models.ImageField(null=True, upload_to='', blank=True)),
                ('info', models.TextField()),
                ('group', models.ForeignKey(to='School.Group')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('info', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='', blank=True)),
                ('discipline', models.ForeignKey(to='School.Discipline')),
                ('group', models.OneToOneField(null=True, blank=True, to='School.Group')),
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
            model_name='comments',
            name='comment_teacher',
            field=models.ForeignKey(to='School.Teacher'),
        ),
    ]
