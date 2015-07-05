from django.forms.models import ModelForm

from .models import Teacher

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('birthdate', 'info', 'discipline', 'photo')
