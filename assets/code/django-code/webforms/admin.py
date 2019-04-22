from django.contrib import admin
from webforms.models import *

class FormAdmin(admin.ModelAdmin):
    fields= ('name','email','phone_number','affiliation','request_body')
    list_display = ('name','email','phone_number','affiliation','request_body')

admin.site.register(Webform, FormAdmin)