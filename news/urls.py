from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.get_news, name='news list'),
    url(r'^(?P<nid>\d+)/$', views.get_news_by_id, name ='get_news_by_id'),
 )