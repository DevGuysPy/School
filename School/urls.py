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

from .views import (index, teacher_detail, group_detail,
                    add_comment, search_room, lesson_detail,
                    student_detail, lesson_detail_edit, student_detail_edit)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,  name="index"),
    url(r'^teacher/(?P<teacher_id>\d+)/$', teacher_detail, name='teacher_detail'),
    url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
    url(r'^student/(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    url(r'^student/(?P<student_id>\d+)/edit/$', student_detail_edit, name='student_detail_edit'),
    url(r'^student/(?P<student_id>\d+)/addmark/$', student_detail, name='add_mark1'),
    url(r'^room/search/$', search_room, name="search_room"),
    # url(r'^search/teacher/$', search_teacher, name="search_teacher"),
    url(r'^lesson/(?P<lesson_id>\d+)/$', lesson_detail, name='lesson_detail'),
    url(r'^lesson/(?P<lesson_id>\d+)/edit/$', lesson_detail_edit, name='lesson_detail_edit'),
    url(r'^lesson/(?P<lesson_id>\d+)/addmark/$', lesson_detail, name='add_mark2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
