# Talk urls
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'talk.views',
    url(r'^$', 'home', name='chat'),
    url(r'^create_post/$', 'create_post'),
)
