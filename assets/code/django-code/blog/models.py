from django.db import models
from meta.models import ModelMeta
from datetime import date
from django.core.urlresolvers import reverse
from image_cropping.fields import ImageRatioField, ImageCropField
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
import re


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(ModelMeta, models.Model):
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    published = models.DateField(default=date.today, help_text='Date that the Entry will be published')
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField("Publish Entry", default=True, help_text='Please click here to publish entry.')
    sticky = models.BooleanField("Make Entry sticky", default=False, help_text='Click here to Post to Front Page')
    listing_picture = ResizedImageField( size=[150,150], crop=['middle','center'], upload_to='uploads/blog/%Y/%m/', blank=True,null=True)
    featured_picture = ResizedImageField(size=[450, 300], crop=['middle', 'center'], upload_to='uploads/blog/%Y/%m/', blank=True, null=True)
    featured_text = models.TextField(blank=True, null=True, max_length=200, help_text='Limited to 200 characters')
    featured_button = models.CharField(blank=True, null=True, max_length=15, verbose_name='Featured Button Text',
                                       help_text='Limited to 15 Characters')
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    objects = EntryQuerySet.as_manager()

    _metadata = {
        'title': 'title',
        'description': 'get_description',
        'keywords': 'get_keywords',
        'image': '/static/main/images/banners/ucla-default-news.png',
        'object_type': 'Article',
        'twitter_type': 'Summary',
        'twitter_site': '@UCLAEPSS',
        'published_time': 'date_published',
        'url': 'get_full_url',
    }

    def get_description(self):
        return "In the Department of Earth, Planetary, and Space Sciences, we seek to understand the Earth and the planets. Our students, researchers, and faculty tackle a wide range of problems, from the Sun to the most distant planets, and from the center of the Earth to the tenuous ionized gases of the solar wind. We probe the interior of the Earth using seismic data, laboratory measurements, and computer modeling. We study both the ancient tectonics of the Earth and its ongoing activity. We explore Earth's upper atmosphere using spacecraft to measure magnetic fields and plasmas. Moving outward from Earth, we study other planets, their interiors, surfaces, atmospheres, and particle and field environments."

    def get_tags(self):
        return "\n".join([tag.name for tag in self.tags.all()])

    def get_keywords(self):
        return self.title.split(' ') + [tag.name for tag in self.tags.all()]

    def get_full_url(self):
        return self.build_absolute_uri(self.get_absolute_url())

    def get_absolute_url(self):
        return reverse('entry-detail', args=(self.slug, self.id))

    class Meta:
        verbose_name = "News Entry"
        verbose_name_plural = "News Entries"
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

    get_tags.short_description = "Tags"
