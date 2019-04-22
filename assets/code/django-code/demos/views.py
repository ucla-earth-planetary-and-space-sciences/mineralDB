
from django.views.generic.list import ListView

from demos.models import Demonstration
from django.shortcuts import render_to_response


def internal_demo_index(request):
    try:
        demo_list = Demonstration.objects.all()
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('demos/demonstration_list.html',{'demo_list': demo_list})

def outreach_demo_index(request):
    try:
        outreach_list = Demonstration.objects.all().filter(is_public=True)
    except ObjectDoesNotExist:
        raise Http404

    return render_to_response('demos/outreach_list.html', {'outreach_list': outreach_list})

