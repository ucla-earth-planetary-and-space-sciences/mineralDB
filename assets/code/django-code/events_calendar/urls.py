from django.conf.urls import *
from .views import *
from courses.models import Quarter

urlpatterns = [
    url(r'^seminars/$', ListView.as_view(
        queryset=SeminarCategory.objects.all(),
        template_name="../templates/events_calendar/seminar-quarter-index.html"),
        name="quarter-index"),
    url(r'^seminars/(?P<category>[-\w]+)/archive/$', ListView.as_view(
        queryset=Quarter.objects.filter(is_visible=True).order_by('-year', 'season'),
        template_name="../templates/events_calendar/quarter-index.html"),
        name="quarter-index"),
    url(r'^seminars/(?P<category>[-\w]+)/$', SeminarCurrent.as_view(), name="seminar-category-index"),
    url(r'^seminars/(?P<category>[-\w]+)/current/$', SeminarCurrent.as_view(),name='seminar-current'),
    url(r'^seminars/(?P<category>[-\w]+)/(?P<quarter>[-\w]+)/$', SeminarCategoryView.as_view(), name="seminar-event-index"),
    url(r'^seminars/(?P<category>[-\w]+)/(?P<quarter>[-\w]+)/(?P<id>\d+)/$', SeminarDetailView.as_view(), name="seminar-event-detail"),
    ]

