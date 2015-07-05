from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline, Student

class Command(BaseCommand):
    help = 'Create groups'

    def handle(self, *args, **options):
        for i in range(30):
            names = ['Petro']
            surnames = ['Petrenko']
            dt = date(1990, 1, 1)
            for k in range(1,37):
                for n in names:
                    for s in surnames:
                        Student.objects.create(
                            name=n,
                            surname=s,
                            birthdate=dt +timedelta(weeks=1),
                            sex="m",
                            group_id=k
                        )


    #         name = models.CharField(max_length=50)
    # surname = models.CharField(max_length=50)
    # birthdate = models.DateTimeField()
    # SEX = (
    #     ('m', "Male"),
    #     ('f', "Female"),
    # )
    # sex = models.CharField(max_length=1, choices=SEX)
    # group = models.ForeignKey(Group)
