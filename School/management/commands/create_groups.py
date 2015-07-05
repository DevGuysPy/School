from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline

class Command(BaseCommand):
    help = 'Create groups'

    def handle(self, *args, **options):
        for i in range(36):
            classes = ['A', 'B', 'C']
            name = "{}-{}".format(i//3 + 1, classes[i % len(classes)])
            Group.objects.create(
                name=name,
                teacher_id=1,
                info='',
                member=30
            )

            # self.stdout.write('Hello!')

            # name = models.CharField(max_length=50)
            # member = models.IntegerField(default=0)
            # info = models.TextField()
            # teacher = models.ForeignKey(Teacher)