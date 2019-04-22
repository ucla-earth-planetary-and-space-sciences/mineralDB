from django.conf.urls import include, url
from .views import IndexView, EntryView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<detail>[-\w\d]+),(?P<id>\d+)/$', view=EntryView.as_view(), name='entry-detail'),
    # url(r'^(?P<category>[-\w\d]+)/$', view=EntryView.as_view(), name='category-detail'),
]
