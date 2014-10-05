from django.conf.urls import patterns, url

from group_yum import views

urlpatterns = patterns('',
    url(r'^$', views.groups, name='index')
)