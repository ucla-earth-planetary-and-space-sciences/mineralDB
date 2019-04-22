from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
import datetime

AFFILIATIONS = (
    ('faculty', 'Faculty',),
    ('researcher', 'Researcher'),
    ('postdoc', 'Postdoctoral Scholar'),
    ('graduate', 'Graduate Student'),
    ('undergrad', 'Undergraduate Student'),
    ('staff', 'Staff'),
    ('other', 'Other'),
    ('N/A', 'I prefer not to say'),
)


class Webform(models.Model):
    name = models.CharField(max_length=100, blank=True, )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    email = models.EmailField(blank=True, )
    affiliation = models.CharField(choices=AFFILIATIONS, max_length=150, blank=False, help_text='<em>* required</em>')
    request_body = models.TextField(max_length=2000, blank=False, help_text='<em>* required</em>')

    def __unicode__(self):
        return self.email + " " + self.request_body[10:]
