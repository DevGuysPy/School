import datetime

from django.shortcuts import render

from .models import Teacher, Lesson


def search(request):
    if request.method == 'POST':
        room_id = int(request.POST['room_id'])
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        lessons = Lesson.objects.filter(room_id=room_id,
                                       start__range=[start_week, end_week])
        # entries = Entry.objects.filter(created_at__range=[start_week, end_week])
    ctx = {
        'lessons': lessons
    }
    return render(request, 'index.html', ctx)