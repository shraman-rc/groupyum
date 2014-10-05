from django.conf.urls import patterns, include, url
from django.contrib import admin
#from groupyum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groupyum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'group_yum.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^group_yum/', 'group_yum.views.groups'),
)
