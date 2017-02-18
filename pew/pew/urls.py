from django.conf.urls import include, url
from django.contrib import admin

from django_markdown import flatpages
from events import urls as event_urls
from django_markdown import urls as md_urls
from django.contrib.flatpages import urls as flat_urls

from main import views

flatpages.register()

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include(event_urls)),
    url(r'^markdown/', include(md_urls)),
    url(r'^pages/', include(flat_urls)),
]