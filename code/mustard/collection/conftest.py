import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mineralDB',
        'USER': 'min_db_user',
        'PASSWORD': 'passwordyall',
        'HOST': 'localhost',
        'PORT': '3306',
    }
