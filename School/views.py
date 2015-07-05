import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Teacher, Lesson, Room, Group, Comments


def result(request):
    ctx = {
        
    }
    return render(request, 'index.html', ctx)


def search_room(request):
    if request.method == 'POST':
        days_w_lessons = []
        date = datetime.date.today()
        monday = date - datetime.timedelta(days=date.weekday())
        room_id = int(request.POST['room_id'])
        for i in range(7):
            date_to_select = monday + timedelta(days=i)
            next_day = monday + timedelta(days=i+1)
            lessons = Lesson.objects.filter(
                room_id=room_id,
                start__range=[date_to_select, next_day])
            days_w_lessons.append(lessons)

    else:
        days_w_lessons = []
    ctx = {
        'week': days_w_lessons
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
    rooms = []
    teachers = []
    groups = []
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
        

    ctx = {
        'rooms': rooms,
        'teachers': teachers,
        'groups': groups,

        
    }
    return render(request, 'index.html', ctx)

def teacher_detail(request, teacher_id=1):
    ctx = {
        'teacher': Teacher.objects.get(id=teacher_id),
        'comments': Comments.objects.filter(comment_teacher_id=teacher_id),
    }
    return render(request, 'teacherprofile.html', ctx)
def group_detail(request, group_id=1):
    ctx = {
        'group': Group.objects.get(id=group_id),
    }
    return render(request, 'groupprofile.html', ctx)

def add_comment(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method == "POST":
        new_comment_text = request.POST['comment_text']
        Comments.objects.create(comment_text=new_comment_text, comment_teacher_id=teacher_id)
        return redirect('teacher_detail', teacher_id=teacher.id) 

    return render(request, 'teacherprofile.html') 
