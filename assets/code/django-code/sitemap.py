from django.contrib.sitemaps import Sitemap
from directory.models import DepartmentMember
from blog.models import Entry
from courses.models import Course
from events_calendar.models import SeminarCategory, SeminarEvent
from research_areas.models import ResearchArea


###############################################################################
#Events App Sitemaps

###############################################################################
class EntrySitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Entry.objects.all().filter(publish=True).order_by('-published')


class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Course.objects.all().filter(active=True).order_by('course_number')


class SeminarMainSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return SeminarCategory.objects.all()


class SeminarEventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return SeminarEvent.objects.all()


################################################################################
# Directory App Sitemaps
#
################################################################################
class StaffSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return DepartmentMember.objects.filter(is_visible=True, user_role='Staff').order_by('last_name')


class FacultySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return DepartmentMember.objects.all().filter(is_visible=True, user_role='Faculty').order_by('last_name')


class StudentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return DepartmentMember.objects.all().filter(is_visible=True, user_role='Student').order_by('last_name')


class ResearcherSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return DepartmentMember.objects.all().filter(is_visible=True, user_role='Researcher').order_by('last_name')

class PostdocSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return DepartmentMember.objects.all().filter(is_visible=True, user_role='Postdoc').order_by('last_name')

################################################################################
# Research Area App Sitemaps
#
################################################################################
class ResearchAreaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ResearchArea.objects.all()
