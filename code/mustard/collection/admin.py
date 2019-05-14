from .models import *
from django.contrib import admin
from django.utils.html import escape
from django.utils import timezone


class SpecimenAdmin(admin.ModelAdmin):

    fields = ('name', 'collection_id','origin_local','chemistry', 'provenance', 'dana_classification','external_link',)
    search_fields = ('all',)
    # list_display = ('title', 'date')
    list_filter = ('name', )


#this works but should use signals rather than overides, because delete is broke

    # def save_model(self, request, obj, form, change):
    #
    #     service = build_service()
    #     start_datetime = obj.event_start
    #     end_datetime = start_datetime + datetime.timedelta(hours=1)
    #
    #     #if it has an ID, we have an instance of event already
    #     if obj.gcal_event_id:
    #         event = service.events().get(calendarId='uicusfjenmhov2ci2rmrvcotcg@group.calendar.google.com', eventId=obj.gcal_event_id).execute()
    #         event['description'] = obj.abstract
    #         updated_event = service.events().update(calendarId='uicusfjenmhov2ci2rmrvcotcg@group.calendar.google.com', eventId=event['id'], body=event).execute()
    #     # if there is no id: create the event and retrieve the id.
    #     else:
    #         event = service.events().insert(
    #             calendarId='uicusfjenmhov2ci2rmrvcotcg@group.calendar.google.com', body={
    #                 'summary': obj.title,
    #                 'description': obj.abstract,
    #                 'start': obj.event_start,
    #                 'end': obj.event_start + datetime.timedelta(hours=2),
    #             }).execute()
    #
    #         obj.gcal_event_id = event.get('id')
    #
    #     super(SeminarEventAdmin, self).save_model(request, obj, form, change)
    #
    # def delete_model(self, request, obj):
    #     service = build_service()
    #     service.events().delete(calendarId='uicusfjenmhov2ci2rmrvcotcg@group.calendar.google.com', eventId=obj.gcal_event_id).execute()
    #     super(SeminarEventAdmin, self).delete_model(request, obj)
    #
    #

admin.site.register(Specimen, SpecimenAdmin)
