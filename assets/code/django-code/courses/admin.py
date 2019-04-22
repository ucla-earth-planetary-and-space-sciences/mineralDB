from .models import *
from django.contrib import admin
from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

DAYS_OF_THE_WEEK = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wedensday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday')

)


# ------------------------------------------------------------------------------
#  Admin Forms for day of the week
# ------------------------------------------------------------------------------
# class CourseAdminForm(forms.ModelForm):
#     days = forms.MultipleChoiceField(choices=DAYS_OF_THE_WEEK)
#
#     class Meta:
#         model = Course
#         fields = '__all__'


# ------------------------------------------------------------------------------#
#  Inine models
# ------------------------------------------------------------------------------#
class InstructorInline(admin.TabularInline):
    model = Instructor
    extra = 0
    fk_name = "course"


#
# class TAInline(admin.TabularInline):
#     model = TA
#     extra = 1
#     fk_name = "course"


# ------------------------------------------------------------------------------#
# Admin models
# ------------------------------------------------------------------------------#
class QuarterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_visible', 'is_archive')
    list_filter = ('is_archive', 'is_visible')
    #
    # def save_model(self, request, obj, form, change):
    #     if len(Quarter.objects.filter(is_archive=False, is_visible=True)) >1:
    #         pass
    #     return super()


class CourseAdmin(admin.ModelAdmin):
    # form = CourseAdminForm
    prepopulated_fields = {"slug": ("course_number", "title")}
    ordering = ['quarter', 'course_number']
    # inlines = [InstructorInline, TAInline]
    inlines = [InstructorInline]
    search_fields = ('course_number', 'title')
    list_display = ('course_number', 'title', 'active', 'level', 'quarter')
    list_filter = ('quarter', 'active')


admin.site.register(Quarter, QuarterAdmin)
admin.site.register(Course, CourseAdmin)
