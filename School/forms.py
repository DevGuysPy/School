from django.forms.models import ModelForm

from .models import Teacher, Lesson, Student

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('birthdate', 'info', 'discipline', 'photo')


class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		fields = ('start', 'group', 'room', 'discipline', 'info', 'teacher')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('birthdate', 'info', 'group', 'photo')