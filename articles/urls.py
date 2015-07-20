from django.conf.urls import url

import views

urlpatterns = (
    url(r'^new/$', views.new_article, name='new_article'),
    url(r'^(?P<article_id>\d+)/$', views.article, name='article_detail'),
)
