from django.conf.urls import *

from courses.views import QuarterListView, CourseListView, CourseDetailView

urlpatterns = [
    url(r'^courses/$', QuarterListView.as_view(), name="quarter-index"),
    url(r'^courses/(?P<quarter>[-\w]+)/$', CourseListView.as_view(), name="course-index"),
    url(r'^courses/(?P<quarter>[-\w]+)/(?P<detail>[-\w]+)/$', CourseDetailView.as_view(), name="course-detail"),
]
