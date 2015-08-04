import datetime
from datetime import timedelta
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from django.db.models import Avg
from django.http import JsonResponse
from .models import (Teacher, Lesson, Room, Group, Comments,
                     Discipline, Student, Mark, StudentActivity)
from .forms import (TeacherForm, LessonForm, StudentForm, MarkForm,
                    GroupForm, UserForm, UserForm2, 
                    FilterStudentsByMarks)

from decimal import Decimal

from articles.models import Article

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
        'articles': reversed(Article.objects.all()),
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


def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Student.objects.filter(group_id=group_id)
    students_count = len(students)

    ctx = {
        'group': group,
        'student': students,
        'students_count': students_count,
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
        Comments.objects.create(comment_text=new_comment_text, \
            comment_teacher_id=teacher_id)
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
        StudentActivity.objects.create(lesson_id=lesson.id, student_id=student,\
            mark_id=mark.id)
        return redirect('lesson_detail', lesson_id=lesson_id)
    ctx = {
        'lesson': lesson,
        'activities': activities,
        'student': student,
        
    }

    return render (request, 'lesson.html', ctx)


def countavgmark(activities):
    all_marks = []

    for s in activities:
        marks = s.mark.number
        all_marks.append(marks)

    start = 0

    for m in all_marks:
        start = start + m

    if all_marks:
        x = Decimal(float(start) / len(all_marks))
        avg = round(x,2)
    else:
        avg = 0

    return avg

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    activities = StudentActivity.objects.filter(student_id=student_id)
    lessons = Lesson.objects.all()
    all_discipline_marks = {} 
    general_average_mark = countavgmark(activities)
    for l in lessons:
        discipline_lessons = l.discipline
        activities_for_marksd = \
            StudentActivity.objects.filter(lesson__discipline=discipline_lessons,\
                student_id=student_id)
        all_discipline_marks[discipline_lessons.name] = \
        countavgmark(activities_for_marksd)

    if request.method == "POST":
        number = request.POST['number']
        reason = request.POST['reason']
        lesson = request.POST['lesson']
        mark = Mark.objects.create(number=number, reason=reason)
        StudentActivity.objects.create(student_id=student.id, lesson_id=lesson,\
            mark_id=mark.id)

        return redirect('student_detail', student_id=student_id)

    ctx = {
        'student': student,
        'activities': activities,
        'lesson': lessons,
        'avgmark': general_average_mark,
        'all_discipline_marks': all_discipline_marks,
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
    students_count = len(students)
    form = FilterStudentsByMarks(request.POST or None)
    students_with_marks = {}

    if request.method == 'POST':
        query = float(request.POST['avg_mark'])
        if form.is_valid():
            all_students = Student.objects.all()
            for s in all_students:
                student_name = s.name + ' ' + s.surname
                student_id = s.id
                students_marks = StudentActivity.objects.filter \
                    (student_id=student_id).aggregate(Avg('mark__number'))\
                        .values()[0]
                if students_marks:
                    x = Decimal(float(students_marks))
                    avg = round(x,2)
                else:
                    avg = 0
                if query <= avg:
                    students_with_marks[student_name] = {'mark': avg, 'id': student_id}
            return JsonResponse({
                'students_with_marks' : students_with_marks,
                'status': 'ok'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'main': form.errors
            })


    ctx = {
        'student': students,
        'students_count': students_count,
    }

    return render (request, 'all_students.html', ctx)


def all_teachers(request):
    teachers = Teacher.objects.all()
    teachers_count = len(teachers)

    ctx = {
        'teachers': teachers,
        'teachers_count': teachers_count,

    }

    return render (request, 'allteachers.html', ctx)

def all_groups(request):
    groups = Group.objects.all()
    groups_count = len(groups)

    ctx = {
        'groups': groups,
        'groups_count': groups_count,
        }

    return render (request, 'all_groups.html', ctx)


def registration(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        account_type = request.POST['account_type']
        form_user = UserForm(request.POST or None)
        form_user2 = UserForm2(request.POST or None)
        if account_type == 'student':
            form_student = StudentForm(request.POST or None)
            if form_user.is_valid():
                user_save = form_user.save()
                user_save.set_password(user_save.password)
                user_save.save()
            ctx_user = {
                'message': form_user.errors,
            }
            if form_user.is_valid():
                user = User.objects.get(username=username)
                if form_student.is_valid():
                    new_student = form_student.save(commit=False)
                    new_student.user = user
                    form_student.save()
                    return JsonResponse({
                        'status': 'ok',
                    })
            else:
                ctx_student = {
                    'status': 'error',
                    'message1': form_student.errors,
                }
                ctx_student.update(ctx_user)
                return JsonResponse(ctx_student)

        if account_type == 'teacher':
            if form_user2.is_valid():
                user_save = form_user2.save()
                user_save.set_password(user_save.password)
                user_save.save()
                user = User.objects.get(username=username)
                host = request.get_host()
                name = request.POST['first_name']
                surname = request.POST['last_name']
                ctx_email = {
                    'name': name,
                    'surname': surname,
                    'user': user,
                    'host': host,
                }
                email_message = render_to_string('email.html', ctx_email)
                send_mail('TeacherRegistration', 'my', settings.EMAIL_BACKEND,
                ['jyvylo@mail.ru'], fail_silently=False, html_message=email_message)
                return JsonResponse({
                    'status': 'ok',
                })
            else:
                return JsonResponse ({
                    'status': 'error',
                    'message': form_user2.errors,
            })
        if account_type == 'other':
            if form_user.is_valid():
                user = form_user.save()
                user.set_password(user.password)
                user.save()
                return JsonResponse({
                    'status': 'ok',
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': form_user.errors,
                })
    ctx = {
        'groups': groups,
    }

    return render(request, 'registration/registration.html', ctx)



def verification(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        Teacher.objects.create(name=user.first_name, surname=user.last_name, user_id=user.id)

    return render(request, 'registration/verification.html')
