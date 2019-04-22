from events_calendar.models import *
from directory.models import *
from django.contrib import admin
from  datetime import datetime, timedelta
import pytz
from django.utils import timezone
from google.oauth2 import service_account
import googleapiclient.discovery
from django.utils.html import escape
#
# prod:
CLIENT_SECRET_FILE = '/var/djangoprojects/production/events_calendar/SVC-Credentials.json'
#CLIENT_SECRET_FILE = '/var/djangoprojects/earthandspace/events_calendar/Gcal-Django-testing.json'

SCOPES = ['https://www.googleapis.com/auth/calendar']

#check for timezones because of weird ass problem with local time.
def is_dst(zonename):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(datetime.utcnow())
    return now.astimezone(tz).dst() != timedelta(0)

def build_service():
    credentials = service_account.Credentials.from_service_account_file(
        CLIENT_SECRET_FILE, scopes=SCOPES, )
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    return service

class SeminarImageAdmin(admin.ModelAdmin):
    pass

class SpeakerInline(admin.TabularInline):
    model = SeminarSpeaker
    extra = 1


class ReadingInline(admin.TabularInline):
    model = SeminarReading
    extra = 1


class SeminarCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": [ "title"]}
    save_as = True


class SeminarEventAdmin(admin.ModelAdmin):
    fields = ('title', 'date', 'time_start', 'time_end', 'location', 'seminar_category', 'quarter', 'description', 'gcal_event_id',
              'gcal_html_link',
              'gcal_calendar_id', 'video_link')
    search_fields = ('title',)
    list_display = ('title', 'quarter', 'seminar_category', 'date' ) # TODO: add sort by speaker name.
    ordering = ['-seminar_category_id']
    list_filter = ('seminar_category', 'date', 'quarter','seminarspeaker__name')
    readonly_fields = ('gcal_event_id', 'gcal_calendar_id', 'gcal_html_link')
    inlines = (SpeakerInline, ReadingInline)



    # TODO: refactor this to use signals, should make including foreign key object data easier

    def save_model(self, request, obj, form, change):
        # this is the encoding thing for scientific characters like permil and delta.
        #obj.description = escape(obj.description)

        service = build_service()

        # sort out timezones holy shit this sucks.
        tzone = is_dst("America/Los_Angeles")

        if tzone:
            tz_offset="-07:00"
        else:
            tz_offset = "-08:00"

        start_datetime = datetime.combine(obj.date, obj.time_start).isoformat() + tz_offset
        end_datetime = datetime.combine(obj.date, obj.time_end).isoformat() + tz_offset


        # get speakers fkey and format for google calendar description
        seminar_speaker = SeminarSpeaker.objects.filter(seminar_id=obj.id)


        speaker_string = ""

        for each in seminar_speaker: speaker_string += str(each.name) + ", <em>" + str(each.institute)+ "</em> - "

        gcal_description = "<strong>Presented by:</strong> {0} \n".format(speaker_string) + \
                           "\n<strong>Location:</strong> <a href='https://www.google.com/maps/place/UCLA+Department+of+Earth,+Planetary,+and+Space+Sciences/@34.0687984,-118.4418977,18.93z/data=!4m12!1m6!3m5!1s0x80c2bc87da1f1c3f:0x2c999ea27d320356!2sGeology+Building!8m2!3d34.0692226!4d-118.441785!3m4!1s0x80c2bc87c2b44b1f:0xdc70f692d889f682!8m2!3d34.0692782!4d-118.4407845'>" \
                           + obj.location + "</a>\n" \
                                            "\n<strong>Abstract:</strong>" + obj.description

        if obj.gcal_event_id:

            if obj.gcal_calendar_id != obj.seminar_category.gcal_calendar_id:
                newcal = obj.seminar_category.gcal_calendar_id
                chgevent = service.events().move(calendarId=obj.gcal_calendar_id, eventId=obj.gcal_event_id,
                                                 destination=newcal).execute()

                event = service.events().get(calendarId=newcal, eventId=obj.gcal_event_id).execute()
                event['summary'] = obj.title
                # event['description'] = (obj.description + speaker['name'] + speaker['institution'])
                event['description'] = gcal_description
                event['start'] = {'dateTime': start_datetime}
                event['end'] = {'dateTime': end_datetime}

                updated_event = service.events().update(calendarId=newcal, eventId=event['id'],
                                                        body=event).execute()

            else:

                samecal = obj.gcal_calendar_id
                event = service.events().get(calendarId=samecal,
                                             eventId=obj.gcal_event_id).execute()
                event['summary'] = obj.title

                event['description'] = gcal_description
                event['start'] = {'dateTime': start_datetime}
                event['end'] = {'dateTime': end_datetime}

                updated_event = service.events().update(calendarId=samecal, eventId=event['id'],
                                                        body=event).execute()

        else:
            event = service.events().insert(calendarId=obj.seminar_category.gcal_calendar_id, body={
                'summary': obj.title,
                'description': gcal_description,
                'start': {'dateTime': start_datetime},
                'end': {'dateTime': end_datetime},
            }).execute()

            obj.gcal_event_id = event.get('id')

        obj.gcal_html_link = event.get('htmlLink')
        obj.gcal_calendar_id = obj.seminar_category.gcal_calendar_id
        #slice the URL to have only the correct embed code here:
        obj.video_link = obj.video_link[17:]


        super(SeminarEventAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        service = build_service()
        service.events().delete(calendarId=obj.gcal_calendar_id,
                                eventId=obj.gcal_event_id).execute()
        super(SeminarEventAdmin, self).delete_model(request, obj)


admin.site.register(SeminarEvent, SeminarEventAdmin)
admin.site.register(SeminarCategory, SeminarCategoryAdmin)
admin.site.register(SeminarImage, SeminarImageAdmin)
