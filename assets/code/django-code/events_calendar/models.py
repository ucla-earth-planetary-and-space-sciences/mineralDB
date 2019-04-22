from django.db import models
from directory.models import DepartmentMember
from courses.models import Quarter
from django.core.urlresolvers import reverse


class SeminarImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/banners/seminar-banners/",
                              blank=True)

    def __unicode__(self):
        return self.name


class SeminarCategory(models.Model):
    title = models.CharField(max_length=100)
    #    description = models.TextField(blank=True)
    gcal_calendar_id = models.CharField(max_length=200,
                                        help_text="if this needs to be updated ever paste the new calendar id into this field.")
    gcal_subscription_link = models.CharField(max_length=200,blank=True, default="#")
    slug = models.SlugField(max_length=200, unique=True)
    course_number = models.CharField(max_length=20)
    faculty = models.ForeignKey(DepartmentMember)

    seminar_image = models.ForeignKey(SeminarImage)

    class Meta:
        verbose_name = "Seminar Category"
        verbose_name_plural = "Seminar Categories"


    def __unicode__(self):
        return (self.title)

    def get_absolute_url(self):
        return reverse('seminar-event-index',
                       args=( self.slug))


class SeminarEvent(models.Model):
    title = models.CharField(max_length=250, verbose_name='Talk Title',
                             help_text='The title of the talk. If no title is set use "TBA - SPEAKER NAME"')
    description = models.TextField(blank=True, verbose_name='Abstract',
                                   help_text='Describe the lecture, or paste an abstract')
    time_start = models.TimeField(auto_now=False, null=True, help_text='what time will the event start?')
    time_end = models.TimeField(auto_now=False, null=True, help_text='what time will it end?')
    location = models.CharField(max_length=100, help_text='where will the event take place?')
    date = models.DateField(null=True, help_text='')
    # google calendar fields:
    gcal_event_id = models.CharField(max_length=200, blank=True, null=True)
    gcal_calendar_id = models.CharField(max_length=200, blank=True, )
    gcal_html_link = models.URLField(verbose_name='Google Calendar Link', blank=True)
    # slug = models.SlugField(max_length=200, unique=True)
    featured_event = models.BooleanField(default=False, help_text='this field will promote the event as Featured')
    seminar_category = models.ForeignKey(SeminarCategory,
                                         related_name="seminar_events",
                                         verbose_name="Seminar Event",
                                         help_text='Which Seminar is this event a part of?')
    video_link = models.CharField(max_length=100, blank=True,
                                  help_text="paste the share link from youtube here; NOT THE EMBED CODE THAT WILL BREAK THINGS. ")
    quarter = models.ForeignKey(Quarter)

    class Meta:
        ordering = ['date','seminar_category']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('seminar-event-detail',
                       args=(self.quarter.slug, self.seminar_category.slug, self.id))

    def get_speaker(self):
        return


class SeminarSpeaker(models.Model):
    seminar = models.ForeignKey(SeminarEvent)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    def __unicode__(self):
        return self.name

class SeminarReading(models.Model):
    seminar = models.ForeignKey(SeminarEvent)
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
