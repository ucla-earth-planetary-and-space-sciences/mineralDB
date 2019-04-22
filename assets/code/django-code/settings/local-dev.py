from development import *

### Database Config ###

# from redactor.widgets import RedactorEditor


ALLOWED_HOSTS = ['local.epss.ucla.edu' ,'media.epss.ucla.edu']

CLIENT_SECRET_FILE = '/var/djangoprojects/earthandspace/events_calendar/SVC-Credentials.json'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'earthandspace',  # Or path to database file if using sqlite3.
        'USER': 'epss_sql',  # Not used with sqlite3.
        'PASSWORD': 'rockyou',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB', },
    }
}

### Directory paths ###

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeOlk8UAAAAAKx77FUiZHtZNI7OoSTRQ_erHwbd'

MEDIA_ROOT = '/var/www/local.epss.ucla.edu/media/'
#PROTECTED_MEDIA_ROOT = '/var/www/media.epss.ucla.edu/protected_media/'
MEDIA_URL = 'http://local.epss.ucla.edu/media/'
#PROTECTED_MEDIA_URL = "http://media.epss.ucla.edu/protected_media/"
STATIC_ROOT = '/var/www/local.epss.ucla.edu/static/'
STATIC_URL = 'http://local.epss.ucla.edu/static/'
#ADMIN_MEDIA_PREFIX = 'http://media.epss.ucla.edu/admin-static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
        'DIRS': ['/var/djangoprojects/earthandspace/templates', ],

    },

]

INTERNAL_IPS = ('192.168.56.1')

