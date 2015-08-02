"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import *

# from .views import (index, teacher_detail, group_detail,
#                     add_comment, room_detail, lesson_detail,
#                     student_detail, lesson_detail_edit, student_detail_edit,
#                     teacher_detail_edit, group_detail_edit, all_students, all_teachers, all_groups,
#                     registration, verification)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,  name="index"),
    url(r'^teacher/(?P<teacher_id>\d+)/$', teacher_detail, name='teacher_detail'),
    url(r'^teacher/(?P<teacher_id>\d+)/edit/$', teacher_detail_edit, name='teacher_detail_edit'),
    url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
    url(r'^group/(?P<group_id>\d+)/edit/$', group_detail_edit, name='group_detail_edit'),
    url(r'^student/(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    url(r'^student/(?P<student_id>\d+)/edit/$', student_detail_edit, name='student_detail_edit'),
    url(r'^student/(?P<student_id>\d+)/addmark/$', student_detail, name='add_mark1'),
    # url(r'^search/teacher/$', search_teacher, name="search_teacher"),
    url(r'^lesson/(?P<lesson_id>\d+)/$', lesson_detail, name='lesson_detail'),
    url(r'^lesson/(?P<lesson_id>\d+)/edit/$', lesson_detail_edit, name='lesson_detail_edit'),
    url(r'^lesson/(?P<lesson_id>\d+)/addmark/$', lesson_detail, name='add_mark2'),
    url(r'^rooms/(?P<room_id>\d+)/$', room_detail, name='room_detail'),
    url(r'^all_school/$', all_school, name='all_school'),
    url(r'^registration/$', registration, name="registration"),
    url(r'^registration/verification/(?P<user_id>\d+)/$', verification, name="verification"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
         {'next_page': '/'}, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^articles/', include('articles.urls')),
]

if settings.SERVE_STATIC:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.SERVE_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

