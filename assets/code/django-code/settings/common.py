import os
import django

# Django settings for earthandspace project.

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

gettext = lambda s: s

DEBUG = False

ADMINS = (

    #holy shit dont ever uncomment this line, 1200 emails in 6 hrs
   #  ('Rod', 'roconnor@epss.ucla.edu'),
)

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'earthandspace',  # Or path to database file if using sqlite3.
        'USER': 'ess_sql',  # Not used with sqlite3.
        'PASSWORD': 'LabAdmin00',  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ucla.epss@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD ='ucla1usc0!'


#this probably needs to be integrated with the gApps domain and service account.
# TODO: this needs a diff oauth flow because of shibboleth

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'epss@g.ucla.edu'
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD ='UC1@EarthP55'


TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

# Additional locations of static files
STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '2%a9-+6flq9^a4xv9v74z#c*zw2sj+nczictvfi=zv$3%j37th'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

# Custom ESS Dashboard Settings
LOGIN_REDIRECT_URL = '/dashboard/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CLIENT_SECRET_FILE = '/var/djangoprojects/staging/events_calendar/GCal-Django-testing.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']






###CKEDITOR SETTINGS ###
CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_RESTRICT_BY_USER=True
CKEDITOR_BROWSE_SHOW_DIRS=True
CKEDITOR_UPLOAD_SLUGIFY_FILENAME=False

DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

CKEDITOR_CONFIGS = {
    'default': {
        'removePlugins': 'stylesheetparser',
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste','-', 'Undo', 'Redo']},

            {'name': 'basicstyles',
             'items': ['Bold', 'Italic',]},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', ]},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


### DJANGO META AUTOMATION OPTIONS: ###
# these are defaults for every page. They should be a baseline for the site as a whole. you can specify extra defaults in each model/view that needs them.

META_SITE_PROTOCOL = 'http'
META_SITE_DOMAIN = "epss.ucla.edu"
META_SITE_NAME = "Earth, Planetary, and Space Sciences Department, UCLA"
META_DEFAULT_KEYWORDS = ["UCLA", "Department of Earth, Planetary, and Space Sciences", "EPSS", "Geology", "Geochemistry", "Space Physics", "Space", "Earth", "Planetology", "Seismology", "Astrobiology", "Oceanography", "Solar System"]
META_USE_SITES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_OG_PROPERTIES = True

#themes for admin page.
JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = False
JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]


