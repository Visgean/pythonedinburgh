from django.conf.urls import url

from .views import EventDetails

urlpatterns = [
    url(
        r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>[a-z0-9_-]+)$',
        EventDetails.as_view(), name='event-details'),
]
