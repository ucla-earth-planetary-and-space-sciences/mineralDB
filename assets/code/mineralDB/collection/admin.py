from django.contrib import admin
from mineralDB.collection.models import specimen

class SpecimenAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
