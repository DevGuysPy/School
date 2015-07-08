from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline

class Command(BaseCommand):
    help = 'Creates lessons for the whole week'
    Lesson.objects.all().delete()

    def handle(self, *args, **options):
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        for i in range(5):
            cur_day = monday + timedelta(days=i)
            start = time(hour=8)
            teachers = Teacher.objects.all()
            if not teachers:
                self.stdout.write("No teachers")
                return
            disciplines = Discipline.objects.all()
            if not disciplines:
                self.stdout.write("No disciplines")
                return
            for l in range(7):
                Lesson.objects.create(
                    start=dtime.combine(cur_day, start) + timedelta(hours=l),
                    # group=Group.objects.get(pk=1),  # also `id=1`
                    group_id=1,
                    # room=Room.objects.get(pk=1),
                    room_id=1,
                    teacher=teachers[l % len(teachers)],
                    discipline=disciplines[l % len(disciplines)]
                )

            self.stdout.write('Hello!')