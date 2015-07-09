#-*- coding: utf-8 -*-
from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline

class Command(BaseCommand):
    help = 'Create Groups'
    Group.objects.all().delete()

    def handle(self, *args, **options):
        teachers = Teacher.objects.all()
        teacher_ids = []
        for l in teachers:
            teacher_ids.append(l.id)
        for i in range(33):
            teacher = i % len(teachers)
            for teacher in teacher_ids:
                classes = ['A', 'B', 'C']
                name = "{}-{}".format(i//3 + 1, classes[i % len(classes)])
                Group.objects.create(
                 name=name,
                 teacher_id=teacher,
                 info='',
                member=30
                )
# -*- coding: utf-8 -*-
