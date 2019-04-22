from django.db import models
from directory.models import DepartmentMember


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    time_start = models.TimeField(auto_now=False)
    time_end = models.TimeField(auto_now=False)
    location = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.title


# Quarter is the main unit of time that is changed.
# Dependant items are course links at the registrar, seminar links, current class links.
# There can be only one quarter that is unarchived and visible at the same time,
# having multiple "active" quarters will break views and things.
#see events calendar.views, the template tags in /Main and courses.views


class Quarter(models.Model):
    SEASONS = (
        (1, 'Fall'),
        (2, 'Winter'),
        (3, 'Spring'),
        (4, 'Summer')
    )

    season = models.IntegerField(choices=SEASONS)
    year = models.IntegerField()
    slug = models.SlugField(max_length=200)
    is_visible = models.BooleanField(
        help_text='This setting determines what quarters will be listed on views that are by quarter. Make all quarters that are not future or too old visible, and set only the current one to be not an archive.')
    is_archive = models.BooleanField(
        help_text='This setting makes the quarter inactive. It will still be visible, if the above box is checked, btu will not be used to determine links or current courses or lectures. There can be only one active and visible quarter at a time, so be careful, this can break things. To make a quarter the current quarter, it should be visible, and not an archive')

    def __unicode__(self):
        return self.slug

    class Meta:
        ordering = ['-year']


class Course(Event):
    COURSE_LEVEL = (
        (0, 'Undergraduate'),
        (1, 'Graduate')
    )

    COURSE_TYPE = (
        (0, 'Lecture'),
        (1, 'Seminar'),
        (2, 'Lab'),
        (3, 'Discussion')
    )

    DAYS_OF_THE_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wedensday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    )

    course_number = models.CharField(max_length=20)
    units = models.CharField(max_length=20)
    course_type = models.IntegerField(choices=COURSE_TYPE)
    outside_link = models.URLField(help_text="URL to Course Website i.e CCLE URL", blank=True)
    active = models.BooleanField(help_text="Status of the course")
    level = models.IntegerField(choices=COURSE_LEVEL, help_text="Level of the course")
    course_id = models.PositiveIntegerField()
    days = models.CharField(max_length=50, blank=True)
    restrictions = models.CharField(max_length=200, blank=True)
    quarter = models.ForeignKey(Quarter, default=33)
    syllabus = models.TextField(blank=True)

    def get_absolute_url(self):
        return "/courses/%s/%s/" % (self.quarter.slug, self.slug)

    def get_course_name(self):
        return "ESS%s - %s" % (self.course_number, self.title)


class Instructor(models.Model):
    course = models.ForeignKey(Course, default=1)
    person = models.ForeignKey(DepartmentMember, default=593)
    office_hours = models.CharField(max_length=100, help_text="Limit 100 characters", blank=True)
    office_hours_location = models.CharField(max_length=100, help_text="Limit 100 characters", blank=True)

    def __unicode__(self):
        return ("%s %s" % (self.person.first_name, self.person.last_name))

# class TA(models.Model):
#     course = models.ForeignKey(Course)
#     person = models.ForeignKey(DepartmentMember)
#     office_hours = models.CharField(max_length=100, help_text="Limit 100 characters", blank=True)
#     office_hours_location = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         verbose_name = "Teaching Assistant"
#         verbose_name_plural = "Teaching Assistants"
#
#     def __unicode__(self):
#         return ("%s %s" % (self.person.first_name, self.person.last_name))
