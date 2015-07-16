# -*- encoding: utf-8 -*-
from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline

class Command(BaseCommand):
    help = 'Create Groups'
    Group.objects.all().delete()

    def handle(self, *args, **options):
        teachers = Teacher.objects.all()
        t_id = []
        for l in teachers:
            t_id.append(l.id)
        for i in range(33):
            teacher = i % len(teachers)
            if teacher in t_id:
                classes = ['A', 'B', 'C']
                name = "{}-{}".format(i//3 + 1, classes[i % len(classes)])
                Group.objects.create(
                    name=name,
                    info='',
                )
