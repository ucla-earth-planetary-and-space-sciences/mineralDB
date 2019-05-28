from .models import *
from django.contrib import admin
from django.utils.html import escape
from django.utils import timezone


class SpecimenAdmin(admin.ModelAdmin):

    fields = ('name', 'collection_id','origin_local','chemistry', 'provenance', 'dana_classification','external_link',)
    search_fields = ('all',)
    # list_display = ('title', 'date')
    list_filter = ('name', )




admin.site.register(Specimen, SpecimenAdmin)
