import json
import os

from django.shortcuts import render
from django.conf import settings

from events.models import Event


def home(request):
    return render(
        request,
        'pew/home.html',
        {
            'upcoming_events': Event.upcoming.all()
        }
    )


def companies(request):
    with open(os.path.join(settings.STATIC_ROOT, 'companies.geojson')) as file:
        geojson = json.loads(file.read())

    companies = [
        f['properties'] for f in geojson['features']
    ]

    return render(
        request,
        'pew/companies.html',
        {
            "companies": companies
        }
    )