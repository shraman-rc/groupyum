from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groupyum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^groups/', 'group_yum.views.groups'),
    url(r'^signup/', 'group_yum.views.signup'),
    url(r'^admin/', include(admin.site.urls)),
)
