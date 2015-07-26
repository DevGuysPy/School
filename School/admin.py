from django.contrib import admin
from School.models import Teacher, Room, Lesson, Group, Discipline, Student, Mark
from articles.models import Article

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass
    # list_display = ('discipline',)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('number',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id',)

# admin.site.register(Teacher)
# admin.site.register(Room)
# admin.site.register(Group)
