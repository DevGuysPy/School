from django.forms.models import ModelForm
from .models import Teacher, Lesson, Student, Mark, Group
from django.contrib.auth.models import User
from django.forms import forms, fields

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('start', 'group', 'room', 'info')


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'middle_name', 'group', 'sex', 'birthdate')


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'surname')

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = ('number', 'reason')

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('info', 'photo')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserForm2(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class FilterStudentsByMarks(forms.Form):
    avg_mark = fields.FloatField(min_value=1, max_value=12)
