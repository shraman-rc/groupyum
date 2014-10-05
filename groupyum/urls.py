from django.conf.urls import patterns, include, url
from django.contrib import admin
#from groupyum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groupyum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'group_yum.views.index',name="index"),
    url(r'^groups/', 'group_yum.views.groups',name="group"),
    url(r'^signup/', 'group_yum.views.signup',name="signup"),
    url(r'^createuser/', 'group_yum.views.createUser',name="createuser"),
    url(r'^admin/', include(admin.site.urls))
)
