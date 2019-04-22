from common import *
#from easy_thumbnails.conf import Settings as thumbnail_settings
#from PIL import pillow
ALLOWED_HOSTS = ['dev.epss.ucla.edu', ]


### DEBUG CONFIG ###
DEBUG = True

### Database Config ###
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'earthandspace_dev_2',  # Or path to database file if using sqlite3.
        'USER': 'ess_sql',  # Not used with sqlite3.
        'PASSWORD': 'xUF8LC38',  # Not used with sqlite3.
        'HOST': '169.232.144.64',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB', },
    }
}

### Directory paths ###
MEDIA_ROOT = '/var/www/dev.epss.ucla.edu/media/'
#PROTECTED_MEDIA_ROOT = '/var/www/media.epss.ucla.edu/protected_media/'
MEDIA_URL = 'https://media.epss.ucla.edu/media/'
#PROTECTED_MEDIA_URL = "http://media.epss.ucla.edu/protected_media/"
STATIC_ROOT = '/var/www/dev.epss.ucla.edu/static/'
STATIC_URL = 'https://media.epss.ucla.edu/static/'
#ADMIN_MEDIA_PREFIX = 'http://media.epss.ucla.edu/admin-static/'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LeOlk8UAAAAAKx77FUiZHtZNI7OoSTRQ_erHwbd'

# Template configuration
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
        'DIRS': ['/var/djangoprojects/development/templates', ],

    },

]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.flatpages.sitemaps',
    'django.contrib.sitemaps',
   # 'easy_thumbnails',
    'image_cropping',
    'jet',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'main',
    'directory',
    'research_areas',
    'blog',
    'courses',
    'events_calendar',
    'bootstrapform',
    'solo',
    'formtools',
    'ckeditor',
    'ckeditor_uploader',
    'adminsortable2',
    'meta',
    'widget_tweaks',
    'webforms',
    'demos'
)

# THUMBNAIL_PROCESSORS = (
#                            'image_cropping.thumbnail_processors.crop_corners',
#                        ) + thumbnail_settings.THUMBNAIL_PROCESSORS


ADMIN_SITE_HEADER = "EPSS Administration Panel"




