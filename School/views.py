import datetime
from datetime import timedelta

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg

from .models import (Teacher, Lesson, Room, Group, Comments,
                     Discipline, Student, Mark, StudentActivity)
from .forms import TeacherForm, LessonForm, StudentForm, MarkForm, GroupForm

from django.contrib.auth.models import User


def room_detail(request, room_id):
    days_w_lessons = []
    date = datetime.date.today()
    monday = date - datetime.timedelta(days=date.weekday())
    room_id = Room.objects.get(id=room_id)
    for i in range(5):
        date_to_select = monday + timedelta(days=i)
        next_day = monday + timedelta(days=i+1)
        lessons = Lesson.objects.filter(
            room_id=room_id,
            start__range=[date_to_select, next_day])
        days_w_lessons.append(lessons)

    ctx = {
        'week': days_w_lessons
    }
    
    return render(request, 'room.html', ctx)


def search_students(name, surname):
    return Student.objects.filter(name__icontains=name,
                                  surname__icontains=surname)


def search_rooms(number):
    try:
        return [Room.objects.get(number=number)]
    except ObjectDoesNotExist:
        return []



def search_teachers(name, surname):
    return Teacher.objects.filter(name__icontains=name,
                                  surname__icontains=surname)


def search_groups(name):
    return Group.objects.filter(name__icontains=name)


def index(request):
    rooms = []
    teachers = []
    groups = []
    students = []
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
                query_words = query.split(' ')
                first, second = query_words[0:2]
            except ValueError:
                first = query
                second = ''
            teachers = list(search_teachers(first, second))
            teachers.extend(list(search_teachers(second, first)))
        if 'students' in request.POST:
            try:
                query_words = query.split(' ')
                first, second = query_words[0:2]
            except ValueError:
                first = query
                second = ''
            students = list(search_students(first, second))
            students.extend(list(search_students(second, first)))

        if 'groups' in request.POST:
            groups = search_groups(query)

    ctx = {
        'rooms': rooms,
        'teachers': teachers,
        'groups': groups,
        'students': students,
    }

    return render(request, 'index.html', ctx)


def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    ctx = {
        'teacher': teacher,
    }

    return render(request, 'teacherprofile.html', ctx)


def teacher_detail_edit(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    form = TeacherForm(
        request.POST or None, request.FILES or None,
        instance=teacher)
    disciplines = Discipline.objects.all()
    ctx = {
        'teacher': teacher,
        'comments': Comments.objects.filter(comment_teacher_id=teacher_id),
        'form': form,
        'disciplines': disciplines,
    }
    if form.is_valid():
        form.save()

    return render(request, 'teacher/edit.html', ctx)


def group_detail(request, group_id=1):
    group = Group.objects.get(id=group_id)
    student = Student.objects.filter(group_id=group_id)

    ctx = {
        'group': group,
        'student': student,

    }
    return render(request, 'groupprofile.html', ctx)


def group_detail_edit(request, group_id):
    group = Group.objects.get(id=group_id)
    student = Student.objects.filter(group_id=group_id)
    form = GroupForm(
        request.POST or None, request.FILES or None,
        instance=group)
    teacher = Teacher.objects.all()
    ctx = {
        'group': group,
        'student': student,
        'form': form,
        'teacher': teacher,
    }
    if form.is_valid():
        form.save()

    return render(request, 'groupprofile_edit.html', ctx)


def add_comment(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method == "POST":
        new_comment_text = request.POST['comment_text']
        Comments.objects.create(comment_text=new_comment_text, comment_teacher_id=teacher_id)
        return redirect('teacher_detail', teacher_id=teacher.id) 

    return render(request, 'teacherprofile.html') 


def lesson_detail_edit(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    form = LessonForm(request.POST or None, instance=lesson)
    ctx = {
        'lesson': lesson,
        'form': form
    }
    if form.is_valid():
        form.save()

    return render (request, 'lesson/edit.html', ctx)


def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    activities = StudentActivity.objects.filter(lesson_id=lesson_id)
    student = Student.objects.all()

    if request.method == "POST":
        student = request.POST['student']
        reason = request.POST['reason']
        number = request.POST['number']
        mark = Mark.objects.create(number=number, reason=reason)
        StudentActivity.objects.create(lesson_id=lesson.id, student=student, mark_id=mark.id)
        return redirect('lesson_detail', lesson_id=lesson_id)
    ctx = {
        'lesson': lesson,
        'activities': activities,
        'student': student,
        
    }

    return render (request, 'lesson.html', ctx)


def student_detail(request, student_id=1):
    student = Student.objects.get(id=student_id)
    activities = StudentActivity.objects.filter(student_id=student_id)
    lessons = Lesson.objects.all()
    # avg_mark = Mark.objects.filter(student_id=student_id).aggregate(Avg('number'))

    if request.method == "POST":
        number = request.POST['number']
        reason = request.POST['reason']
        lesson = request.POST['lesson']
        mark = Mark.objects.create(number=number, reason=reason)
        StudentActivity.objects.create(student_id=student.id, lesson_id=lesson, mark_id=mark.id)
        return redirect('student_detail', student_id=student_id)

    ctx = {
        'student': student,
        'activities': activities,
        'lesson': lessons,
        # 'average_mark':avg_mark['number__avg'],
    }

    return render(request, 'studentprofile.html', ctx)


def student_detail_edit(request, student_id=1):
    student = Student.objects.get(id=student_id)
    activities = StudentActivity.objects.filter(student_id=student_id)
    form = StudentForm(request.POST or None, request.FILES or None,
                        instance=student)
    form_mark = MarkForm(request.POST or None, request.FILES or None,
                        instance=student)
                        
    groups = Group.objects.all()
    lessons = Lesson.objects.all()

    ctx = {
        'student': student,
        'form': form,
        'groups': groups,
        'activities': activities,
        'form_mark': form_mark,
        'lessons': lessons,
    }
    if form_mark.is_valid():
        form_mark.save()

    if form.is_valid():
        form.save()
    
    return render(request, 'student/edit.html', ctx)


def all_students(request):
    students = Student.objects.all()
    ctx = {
        'student': students,
    }

    return render (request, 'all_students.html', ctx)


def all_teachers(request):
    teachers = Teacher.objects.all()

    ctx = {
        'teachers': teachers
    }

    return render (request, 'allteachers.html', ctx)

def all_groups(request):
    groups = Group.objects.all()

    ctx = {
        'groups': groups
        }

    return render (request, 'all_groups.html', ctx)

def registration(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        surname = request.POST['surname']
        birthdate = request.POST['birthdate']
        sex = request.POST['sex']
        group = request.POST['group']
        user = User.objects.create_user(username=username, email=email, password=password)
        Student.objects.create(name=name, surname=surname, birthdate=birthdate, sex=sex, group_id=group, user_id=user.id)
        return redirect('/login/')
    ctx = {
        'groups': groups,
    }
    return render(request, 'registration/registration.html', ctx)
