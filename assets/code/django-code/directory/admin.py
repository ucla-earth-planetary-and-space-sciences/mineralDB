from directory.models import *
from django.contrib import admin
from research_areas.models import ResearchArea


class ResearchAreaRelationshipInline(admin.TabularInline):
    model = ResearchArea
    extra = 1


class DegreeInline(admin.TabularInline):
    model = Degree
    extra = 1


class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 1


class DepartmentMemberAdmin(admin.ModelAdmin):

    fields = ('user_role', 'first_name', 'last_name', 'slug', 'email', 'username',
              'is_visible', 'location', 'phone_number', 'title', 'profile_image', 'thumbnail_image')
    list_display = ('first_name', 'last_name', 'email', 'is_visible', 'user_role')
    list_filter = ('is_visible', 'user_role')
    search_fields = ['first_name', 'last_name', 'title', 'user_role']
    prepopulated_fields = {"slug": ("first_name", "last_name",)}
    inlines = [WebsiteInline, DegreeInline]
    ordering = ['-is_visible','user_role','last_name']

class AlumnusAdmin(admin.ModelAdmin):
    # fields = ('first_name', 'last_name', 'degree', 'year_graduated', 'thesis', 'institution', 'title', 'advisor', 'first_destination_position','first_destination_institution' )
    list_display = ('first_name', 'last_name', 'year_graduated', 'advisor')
    list_filter = ('year_graduated', 'institution', 'advisor')
    search_fields = ['first_name', 'last_name', 'year_graduated']

class BoardAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'title']


admin.site.register(BoardMember, BoardAdmin)
admin.site.register(DepartmentMember, DepartmentMemberAdmin)
admin.site.register(Alumnus, AlumnusAdmin)
