from django.conf.urls import *
import django.contrib.sitemaps
from django.views.generic import ListView
from django.conf import settings
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps import views as sitemap_views
from sitemap import *
from main import views as homepage_views
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap




admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    # Event Sitemaps
    'news': EntrySitemap,
    'courses': CourseSitemap,
    'seminar-main-info': SeminarMainSitemap,
    'seminar-events': SeminarEventSitemap,
    # Directory Sitemaps
    'staff': StaffSitemap,
    'faculty': FacultySitemap,
    'students': StudentSitemap,
    'researchers': ResearcherSitemap,
    # Research Area Sitemap
    'research-areas': ResearchAreaSitemap
}

urlpatterns = [

    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # index
    url(r'^$', homepage_views.main_index, name='main_view'),

    # directory
    url(r'^people/', include('directory.urls')),

    # research areas
    url(r'^research-areas/', include('research_areas.urls')),

    # news
    url(r'^news/', include('blog.urls')),

    # courses
    url(r'^', include('courses.urls')),

    # events_calendar
    url(r'^', include('events_calendar.urls')),

    #hook up wysiwyg editor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^', include('webforms.urls')),

    url( r'^', include('demos.urls'))
]

urlpatterns += [

    url(r'^sitemap\.xml$', sitemap_views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
