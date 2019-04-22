from django.db import models
from solo.models import SingletonModel
from image_cropping.fields import ImageRatioField, ImageCropField
from datetime import date
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth.models import User, Group
from django_resized import ResizedImageField


class StaticLinks(SingletonModel):
    scheduleOfClasses = models.URLField(max_length=350, verbose_name="Schedule of classes Link")
    courseCatalog = models.URLField(max_length=350, verbose_name="Course Catalog Link")
    GivingLinkSwitch = models.BooleanField(default=True, verbose_name='Featured Articles Giving Link')

    def __unicode__(self):
        return u"Static Links"

    class Meta:
        verbose_name = "Static Links"


class SeminarLinks(models.Model):
    name = models.CharField(max_length=350)
    slug = models.SlugField(max_length=200, unique=True)
    link = models.URLField(max_length=350)

    def __unicode__(self):
        return u"Seminar Links"

    class Meta:
        verbose_name = "Seminar Link"
        verbose_name_plural = "Seminar Links"


class Banner(models.Model):
    banner_image = ResizedImageField(size=[1140, 475], crop=['middle', 'center'],

                                        upload_to='banners/desktop/', blank=True, null=True)
    mobile_banner = ResizedImageField(size=[768, 400], crop=['middle', 'center'],
                                        upload_to='banners/mobile/', blank=True, null=True)

    title_text = models.CharField(max_length=50, help_text='Maximum characters is 50')
    description_text = models.CharField(max_length=140, help_text='Maximum characters is 140', blank=True)
    url = models.URLField(max_length=2000)
    enable_banner = models.BooleanField(default=False, help_text="Click here to enable banner")
    date = models.DateField(default=date.today, help_text='Date Banner will be published')
    banner_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['banner_order']

    def __unicode__(self):
        return self.title_text


class FlatPageEditGroup(models.Model):
    name = models.CharField(max_length=60, help_text='Enter A Name for the Group', blank=True)
    members = models.ManyToManyField(User, help_text='Select one or more users to access the following pages')
    page = models.ManyToManyField(FlatPage, help_text='These are the pages that this group can edit')
    def __unicode__(self):
        return self.name
