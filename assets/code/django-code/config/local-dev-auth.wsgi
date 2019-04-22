import os, sys
import site
import base64

sys.path.append('/var/djangoprojects/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'earthandspace.settings.local-dev'
sys.stdout = sys.stderr

from django import db
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
def allow_access(environ, host):
    """
    Authentication handler that checks if user is logged in
    """
    # Fake this, allow_access gets a stripped environ
    environ['wsgi.input'] = None
    request = WSGIRequest(environ)
    errors = environ['wsgi.errors']

    print >> sys.stderr, "%s" % request.COOKIES.get('sessionid')
    session_key = request.COOKIES.get('sessionid')
    
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)

    print >> sys.stderr, "%s" % user
    
    try:
        if user.is_authenticated:
            return True
        else:
            return False
    except Exception as e:
        errors.write('Exception: %s\n' % e)
        return False

    finally:
        db.connection.close()



  