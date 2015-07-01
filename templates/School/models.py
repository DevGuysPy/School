import pytz
from datetime import timedelta, datetime as dtime

from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    # room = models.ForeignKey(Room)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.IntegerField(default=0)
    info = models.TextField()
    discipline = models.ForeignKey(Discipline)

    class Meta():
        db_table = 'teacher'

    def __str__(self):
        return self.name 

class Group(models.Model):
    name = models.CharField(max_length=50)
    member = models.IntegerField(default=0)
    info = models.TextField()
    teacher = models.ForeignKey(Teacher)
    class Meta():
        db_table = 'group'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    SEX = (
        ('m', "Male"),
        ('f', "Female"),
    )
    sex = models.CharField(max_length=1, choices=SEX)
    group = models.ForeignKey(Group)
    # group _id



class Room(models.Model):
    seats = models.IntegerField()
    def __str__(self):
        return str(self.id)


class Lesson(models.Model):
    start = models.DateTimeField()
    group = models.ForeignKey(Group)
    room = models.ForeignKey(Room)
    teacher = models.ForeignKey(Teacher)
    discipline = models.ForeignKey(Discipline)

    def __str__(self):
        return "{} в {}".format(self.discipline.name, self.start)

    def end(self):
        return self.start + timedelta(minutes=45)

    def is_now(self):
        # datetime.now(pytz.utc)
        return self.start < dtime.now(pytz.utc) < self.end()



# class MyGroup1(models.Model):
#     name =
#     student = models.ForeignKey(MyStudent1)
#     group_director


# class MyStudent1(models.Model):
#     name =
#
# # --------------------
#
# class MyGroup2(models.Model):
#     name =
#     group_director =
#
# class MyStudent2(models.Model):
#     name =
#     surname =
#     birthdate =
#     group = models.ForeignKey(MyGroup2)
#
# # 1-A       Volodymyr
# # 2-A
