from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_markdown import flatpages


flatpages.register()

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
)
