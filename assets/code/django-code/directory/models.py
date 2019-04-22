from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_resized import ResizedImageField

USER_ROLES = (
    ('Student', 'Student'),
    ('Faculty', 'Faculty'),
    ('Staff', 'Staff'),
    ('Researcher', 'Researcher'),
    ('Postdoc', 'Postdoc'),

)


class DepartmentMember(User):
    is_visible = models.BooleanField('Visible in Directory', default=True,
                                     help_text="Designates if person shows up in directory.")
    title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)

    thumbnail_image = ResizedImageField(size=[150, 150], crop=['middle', 'center'],
                                        upload_to='uploads/directory/thumbnail_pictures/', blank=True)
    profile_image = ResizedImageField(size=[600, 600], crop=['middle', 'center'],
                                      upload_to='uploads/directory/profile_pictures/', blank=True)
    slug = models.SlugField(max_length=200, help_text="Required. Part of the URL for the directory info.")
    user_role = models.CharField(max_length=80, choices=USER_ROLES, default='Student')

    def full_name(obj):
        return ("%s %s" % (obj.first_name, obj.last_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse(str(self.user_role).lower() + '-detail', args=(self.id,))


class Website(models.Model):
    person = models.ForeignKey(DepartmentMember)
    website_label = models.CharField(max_length=200)
    website_url = models.URLField(max_length=500)


class Degree(models.Model):
    person = models.ForeignKey(DepartmentMember)
    degree_level = models.CharField('Degree Level', max_length=200)
    year = models.PositiveIntegerField(help_text="Year when the Degree was awarded")
    school = models.CharField('School', max_length=200, help_text='School where Degree was awarded')


class Alumnus(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    year_graduated = models.CharField(max_length=200, blank=True)
    thesis = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    advisor = models.CharField(max_length=200, blank=True)
    first_destination_position = models.CharField(max_length=200, blank=True, verbose_name='First Destination Position')
    first_destination_institution = models.CharField(max_length=200, blank=True,
                                                     verbose_name='First Destination Institution')

    def full_name(obj):
        return ("%s %s" % (obj.first_name, obj.last_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

    class Meta:
        verbose_name = "Alumnus/Alumna"
        verbose_name_plural = "Alumni"
        ordering = ['last_name']

class BoardMember(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=25, blank=True)
    profile_image = ResizedImageField(size=[150, 150], crop=['middle', 'center'],
                                        upload_to='uploads/directory/thumbnail_pictures/', blank=True)
    #called this to stop emeritus title from messing things up. should be title.
    official_title = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    def full_name(obj):
        return ("%s %s" % (obj.first_name, obj.last_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Board"
        ordering = ['last_name']
