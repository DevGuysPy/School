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
        fields = ('birthdate', 'name', 'surname')

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = ('number', 'reason')

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('info', 'photo')

