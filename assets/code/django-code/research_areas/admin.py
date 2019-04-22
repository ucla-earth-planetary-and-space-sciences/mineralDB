from django.contrib import admin
from research_areas.models import ResearchArea
from research_areas.models import *


class ResearchAreaRelationshipInline(admin.StackedInline):
    model = ResearchArea.faculty.through
    extra = 0
    verbose_name = "Research Area Member"
    verbose_name_plural = "Research Area Members"


class ResearchAdmin(admin.ModelAdmin):

    fields = ('name', 'details', 'image', 'banner', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ResearchAreaRelationshipInline,)
    ordering=['name']


admin.site.register(ResearchArea, ResearchAdmin)
