#!/usr/bin/env python
from django.core.management import setup_environ
from sys.earthandspace import settings
from directory.models import Faculty
from whrandom import choice
import string

setup_enviromen(settings)


def GenPasswd():
    chars = string.letters + string.digits
    for i in range(8):
        newpasswd = newpasswd + choice(chars)
    return newpasswd


def GenPasswd2(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])


password = GenPassword()
print password

user = User.objects.get(username__exact='msimpson')
user.set_password(password)
user.save()
