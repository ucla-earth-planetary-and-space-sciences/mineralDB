from django.conf.urls import *
from webforms.models import *
from webforms.views import *

urlpatterns = [
    url(r'^feedback/$', new_feedback_submission, name='feedback'),
    # url(r'^success/', view=FormDetail.as_view(), name='FromDetail')
    ]


