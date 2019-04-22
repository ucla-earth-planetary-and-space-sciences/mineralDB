from django.conf.urls import *
from django.views.generic import ListView, DetailView
from research_areas.models import *
from research_areas.views import *

urlpatterns = [

    url(r'^$', ListView.as_view(template_name="research_areas/index.html", model=ResearchArea)),
    url(r'^(?P<slug>[-\w\d]+)/$', ResearchAreaDetailView.as_view(), name="research-area-detail")
]
