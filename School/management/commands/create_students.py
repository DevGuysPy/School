# -*- encoding: utf-8 -*-
from datetime import date, datetime as dtime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from School.models import Lesson, Group, Room, Teacher, Discipline, Student
import random

class Command(BaseCommand):
    help = 'Create Students'
    Student.objects.all().delete()

    def handle(self, *args, **options):
        grup_count = len(Group.objects.all())
        names_male = ['Petro','Ivan','Roman','Andre','Sergij','Volodymyr']
        names_female= ['Oksana','Marija','Natalja','Anna','Svitlana','Katja']
        sex_m_f = ['m','f']
        surnames = ['Petrenko','Nikolaenko','Sydorenko','Bondarenko','Poroshenko','Tymoshenko','Gubenko']
        for i in range(10):
            si = random.randint(0,1)
            sexmf = sex_m_f[si]
            for dd, s in enumerate(surnames):
                # вибираємо випадкові імена з масивів імен чоловіків або жінок
                if si==0:
                    name_male_female = names_male[random.randint(0,len(names_male)-1)]
                else:
                    name_male_female = names_female[random.randint(0,len(names_female)-1)]
                # формуємо псевдо випадкові дати народження учнів
                # дні
                if dd>30:
                    dd = 1
                # місяці
                m = random.randint(0,11)
                dt = date(1990+i, m+1, dd+1)
                data_nar = dt +timedelta(days=1)
                # розпихуємо учнів по випадкових наявних групах
                nom_grup = random.randint(0,grup_count)
                Student.objects.create(
                    name=name_male_female,
                    surname=s,
                    birthdate=data_nar,
                    sex=sexmf,
                    group_id=nom_grup
                )
