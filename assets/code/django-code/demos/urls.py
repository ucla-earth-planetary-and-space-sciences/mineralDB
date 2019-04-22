from django.conf.urls import *


from demos.views import *


urlpatterns = [

    # url(r'^demos/$', DemoListView.as_view(), name=''),
    url(r'^demos/$', internal_demo_index, name='demo-index'),
    url(r'^outreach/resources/$', outreach_demo_index, name='outreach-index')

]
