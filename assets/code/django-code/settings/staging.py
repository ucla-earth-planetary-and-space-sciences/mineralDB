from production import *

### DEBUG CONFIG ###
DEBUG = True

CLIENT_SECRET_FILE = '/var/djangoprojects/staging/events_calendar/SVC-Credentials.json'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LeOlk8UAAAAAKx77FUiZHtZNI7OoSTRQ_erHwbd'
### Database Config ###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'earthandspace_staging',  # Or path to database file if using sqlite3.
        'USER': 'ess_sql',  # Not used with sqlite3.
        'PASSWORD': 'xUF8LC38',  # Not used with sqlite3.
        'HOST': '169.232.144.64',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB', }
    }
}
### Directory paths ###
MEDIA_ROOT = '/var/www/staging.epss.ucla.edu/media/'
#PROTECTED_MEDIA_ROOT = '/var/www/media.epss.ucla.edu/protected_media/'
MEDIA_URL = 'https://staging.epss.ucla.edu/media/'
#PROTECTED_MEDIA_URL = "http://media.epss.ucla.edu/protected_media/"
STATIC_ROOT = '/var/www/staging.epss.ucla.edu/static/'
STATIC_URL = 'https://staging.epss.ucla.edu/static/'
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
        'DIRS': ['/var/djangoprojects/staging/templates', ],

    },

]
