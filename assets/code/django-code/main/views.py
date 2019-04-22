from django.shortcuts import render
from events_calendar.models import SeminarEvent
from blog.models import Entry
from main.models import Banner
from datetime import date as date_function

def main_index(request):
    today = date_function.today()
    try:
        announcement_list = Entry.objects.filter(publish=True).order_by('-published')[:4]
        featured_list = Entry.objects.filter(sticky=True).order_by('-published')[:3]
        event_list = SeminarEvent.objects.filter(date__gte=today).order_by('date', 'time_start')[:5]
       #event_list = SeminarEvent.objects.all()[:5]
        banner_list = Banner.objects.filter(date__lte=today).filter(enable_banner=True).order_by('banner_order')
    except Entry.DoesNotExist or SeminarEvent.DoesNotExist or Banner.DoesNotExist:
        raise http404

    context = {
        'announcement_list': announcement_list,
        'event_list': event_list,
        'featured_list': featured_list,
        'banner_list': banner_list
    }
    return render(request, 'home.html', context)
