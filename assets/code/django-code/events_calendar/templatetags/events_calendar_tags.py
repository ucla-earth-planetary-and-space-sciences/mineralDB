from django import template
from events_calendar.models import SeminarCategory, SeminarEvent
from courses.models import Quarter

register = template.Library()


@register.simple_tag
def get_events_calendar_list():
    events_calendar_list = SeminarCategory.objects.exclude(title__icontains='distinguished')
    return events_calendar_list


@register.simple_tag
def get_current_quarter():
    current_quarter = Quarter.objects.get(is_archive=False, is_visible=True)
    return current_quarter


# this tag looks to see if there are any lectures under the current quarter that have distinguished in their titles. THis is to remove the Distingished alumni and faculty lectures from the tope level menu when they are not offered,
# btu when you crreate on in an active quarter, they will automatically be added back to the
@register.simple_tag
def get_special_events():
    special_events = SeminarCategory.objects.filter(title__icontains='distinguished')
    current_quarter = Quarter.objects.get(is_archive=False, is_visible=True)
    queryset_out = SeminarEvent.objects.filter(seminar_category_id=special_events[0].id).filter(
        quarter_id=current_quarter.id)

    if len(queryset_out) > 0:
        return special_events
    else:
        pass


@register.simple_tag
def get_special_events():
    special_events = SeminarCategory.objects.filter(title__icontains='faculty')
    current_quarter = Quarter.objects.get(is_archive=False, is_visible=True)
    queryset_out = SeminarEvent.objects.filter(seminar_category_id=special_events[0].id).filter(
        quarter_id=current_quarter.id)

    if len(queryset_out) > 0:
        return special_events
    else:
        pass
