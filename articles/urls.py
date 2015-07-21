from django.conf.urls import url

from .views import new_article, article

urlpatterns = (
    url(r'^new/$',new_article, name='new_article'),
    url(r'^(?P<article_id>\d+)/$',article, name='article_detail'),
)
