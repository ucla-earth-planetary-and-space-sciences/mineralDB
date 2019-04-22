from __future__ import unicode_literals
from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Demonstration(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = ResizedImageField(size=[700, 500], crop=['middle', 'center'], upload_to="uploads/demos/", blank=True)
    video_link = models.CharField(max_length=100, blank=True, help_text="paste the share link from youtube here; NOT THE EMBED CODE THAT WILL BREAK THINGS. ")
    is_public = models.BooleanField(default=False, help_text="check this box to have the demo show up under the outreach tab as well as the full demo listing")

    def __unicode__(self):
        return (self.name)


