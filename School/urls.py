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

from .views import index, teacher_detail, group_detail, add_comment # , search_room, search_teacher

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,  name="index"),
    url(r'^teacher/(?P<teacher_id>\d+)/$', teacher_detail, name='teacher_detail'),
    url(r'^group/(?P<group_id>\d+)/$', group_detail, name='group_detail'),
    url(r'^teacher/(?P<teacher_id>\d+)/addcomment/$', add_comment, name='add_comment'),
    # url(r'^search/room/$', search_room, name="search_room"),
    # url(r'^search/teacher/$', search_teacher, name="search_teacher"),
]
