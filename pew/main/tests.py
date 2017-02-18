from django.test import TestCase

from datetime import timedelta
from django.test.client import RequestFactory
from django.test import Client
from django.utils import timezone

from events.models import Event
from . import views


class HomeViewTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        self.events = [
            Event.objects.create(
                title='Future Event',
                description='this event is going to be great.',
                event_dt=timezone.now() + timedelta(seconds=5),
                location='The Pub',
                published=True,
                slug='new-event',
            )
        ]

    def test_home_context_dict(self):
        response = self.client.get('/')
        self.assertSequenceEqual(
            response.context['upcoming_events'],
            self.events
        )

    def test_home_dict_contains_upcoming_events(self):
        request = self.factory.get('/')
        response = views.home(request)
        self.assertEqual(response.status_code, 200)
