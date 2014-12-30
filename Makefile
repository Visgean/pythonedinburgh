export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=pew

.PHONY: test

test:
	flake8 pew/pew --ignore=E124,E501,E127,E128
#coverage run --branch --source=pew/pew `which django-admin.py` test pew.tests
#coverage report