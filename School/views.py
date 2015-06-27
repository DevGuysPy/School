import datetime

from django.shortcuts import render

from .models import Teacher, Lesson, Room, Group


def index(request):
    ctx = {

    }
    return render('index.html', ctx)


def search_room(request):
    if request.method == 'POST':
        # days_w_lessons = []
        # for i in range(7):
        #     # monday = ... # 29.06.2015 00:00
        #     date_to_select = monday + timedelta(days=i)
        #     next_day = monday + timedelta(days=i+1)
        #     lessons = Lesson.objects.filter(
        #         room_id=room_id,
        #         start__range=[start_week, end_week])
        #     days_w_lessons.append(lessons)

        room_id = int(request.POST['room_id'])
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        lessons = Lesson.objects.filter(room_id=room_id,
                                       start__range=[start_week, end_week])
        # entries = Entry.objects.filter(created_at__range=[start_week, end_week])
    else:
        lessons = []
    ctx = {
        'lessons': lessons
    }
    return render(request, 'search/room.html', ctx)


def search_rooms(room_id):
    return [Room.objects.get(id=room_id)]


def search_teachers(name, surname):
    return Teacher.objects.filter(name__icontains=name,
                                  surname__icontains=surname)

def search_groups(name):
    return Group.objects.filter(name__icontains=name)

def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        if 'rooms' in request.POST:
            try:
                rooms = search_rooms(int(query))
            except ValueError:
                rooms = []

        if 'teachers' in request.POST:
            # *_ - unpacking
            # save all other parts to _ as array
            # so that
            # "Sergey Vlad Potcht"
            # =>
            # first = "Sergey"
            # second = "Vlad"
            # _ = ['Pocht']
            try:
                first, second, *_ = query.split(' ')
            except ValueError:
                first = query
                second = ''
            teachers = list(search_teachers(first, second))
            teachers.extend(list(search_teachers(second, first)))

        if 'groups' in request.POST:
            groups = search_groups(query)
    else:
        rooms = []
        teachers = []
        groups = []

    ctx = {
        'rooms': rooms,
        'teachers': teachers,
        'groups': groups,
    }
    return render(request, 'index.html', ctx)