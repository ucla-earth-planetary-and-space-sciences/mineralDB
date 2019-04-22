import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.development'

path = '/var/djangoprojects/development'

if path not in sys.path:
   sys.path.append(path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()