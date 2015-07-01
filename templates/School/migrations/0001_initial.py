# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('discipline', models.ForeignKey(to='School.Discipline')),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateTimeField()),
                ('sex', models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female')])),
                ('group', models.ForeignKey(to='School.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
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
    ]
