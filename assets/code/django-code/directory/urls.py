from django.conf.urls import url
from django.views.generic import ListView
#from directory.models import Staff
from directory.views import *


urlpatterns = [
    url(r'^staff/$', staff_index, name='staff-index'),
    url(r'^staff/(?P<staff_id>\d+)/$',staff_detail, name='staff-detail'),
    url(r'^researchers/$', researcher_index, name='researcher-index'),
    url(r'^researchers/(?P<researcher_id>\d+)/$',researcher_detail, name='researcher-detail'),
    url(r'^postdocs/$', postdoc_index, name='postdoc-index'),
    url(r'^postdocs/(?P<postdoc_id>\d+)/$', postdoc_detail, name='postdoc-detail'),
    url(r'^faculty/$', faculty_index, name='faculty-index'),
    url(r'^faculty/(?P<faculty_id>\d+)/$',faculty_detail, name='faculty-detail'),
    url(r'^students/$', student_index, name='student-index'),
    url(r'^students/(?P<student_id>\d+)/$',student_detail, name='student-detail'),
    url(r'^alumni/$', alumni_index, name='alumni-index'),
    url(r'^board/$', board_index, name='board-index'),
    url(r'^board/(?P<board_id>\d+)/$', board_detail, name='board-detail'),
]