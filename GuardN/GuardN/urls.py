from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GuardN.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^devGuardN/', include('devGuardN.urls', namespace="devGuardN")),
    url(r'^admin/', include(admin.site.urls)),
)
