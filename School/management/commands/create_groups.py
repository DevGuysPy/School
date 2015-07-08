from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline

class Command(BaseCommand):
    help = 'Create groups'
    Group.objects.all().delete()

    def handle(self, *args, **options):
        teachers = Teacher.objects.all()
        for i in range(33):
            classes = ['A', 'B', 'C']
            name = "{}-{}".format(i//3 + 1, classes[i % len(classes)])
            teacher = i % len(teachers)
            Group.objects.create(
                name=name,
                teacher_id=teacher,
                info='',
                member=30
            )

            # self.stdout.write('Hello!')

            # name = models.CharField(max_length=50)
            # member = models.IntegerField(default=0)
            # info = models.TextField()
            # teacher = models.ForeignKey(Teacher)