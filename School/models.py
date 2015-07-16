# -*- encoding: utf-8 -*-
import pytz
from datetime import timedelta, datetime as dtime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Mark(models.Model):
    number = models.IntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(12)])
    reason = models.CharField(max_length=150)



class StudentActivity(models.Model):
    lesson = models.ForeignKey('Lesson', null=True)
    student = models.ForeignKey('Student')
    mark = models.OneToOneField('Mark')



class Discipline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    # room = models.ForeignKey(Room)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    info = models.TextField()
    discipline = models.ForeignKey(Discipline)
    photo = models.ImageField(blank=True, null=True)
    group = models.OneToOneField('Group', null=True, blank=True)

    class Meta():
        db_table = 'teacher'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    
    class Meta():
        db_table = 'group'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    SEX = (
        ('m', "Male"),
        ('f', "Female"),
    )
    sex = models.CharField(max_length=1, choices=SEX)
    group = models.ForeignKey(Group)
    photo = models.ImageField(blank=True, null=True)
    info = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, null=True)
    activities = models.ManyToManyField('Lesson', through='StudentActivity', related_name='activities')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class Room(models.Model):
    seats = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    start = models.DateTimeField()
    group = models.ForeignKey(Group)
    room = models.ForeignKey(Room)
    teacher = models.ForeignKey(Teacher)
    discipline = models.ForeignKey(Discipline)
    info = models.TextField()

    def __str__(self):
        return "{} в {}".format(self.discipline.name, self.start)

    def __unicode__(self):
        return u"{} в {}".format(self.discipline.name, self.start)

    def end(self):
        return self.start + timedelta(minutes=45)

    def is_now(self):
        # datetime.now(pytz.utc)
        return self.start < dtime.now(pytz.utc) < self.end()


class Comments(models.Model):
    comment_text = models.TextField()
    comment_teacher = models.ForeignKey(Teacher)

    class Meta():
        db_table = 'comments'
