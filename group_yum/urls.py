from django.conf.urls import patterns, url

from group_yum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='homepage'),
    url(r'^group_yum/$', views.groups, name='groups')
)
