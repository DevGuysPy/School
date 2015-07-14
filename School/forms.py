from django.forms.models import ModelForm

from .models import Teacher, Lesson, Student, Mark, Group

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('birthdate', 'info', 'discipline', 'photo')


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('start', 'group', 'room', 'info')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('birthdate', 'info', 'group', 'photo')

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = ('number', 'lesson', 'reason')

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'info', 'photo')