from {{prname}}.settings import *


STATIC_ROOT = '/home/{{prname}}/webstatic'
MEDIA_ROOT = '/home/{{prname}}/webstatic/media'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{dbuser}}',
        'USER': '{{dbuser}}',
        'PASSWORD': '{{prname}}',
        'HOST': '',
        'PORT': '',
    }
}
