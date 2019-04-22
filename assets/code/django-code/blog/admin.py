from django.db import models
from django.forms import TextInput, Textarea
from django.contrib import admin
from django.forms import ModelForm

from .models import Entry, Tag, Category
from image_cropping.admin import ImageCroppingMixin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BodyForm(ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'




class EntryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})},
    }
    list_display = ('title', 'published', 'get_tags', 'category', 'sticky')
    list_filter = ('sticky','category',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',), }
    form = BodyForm
    fieldsets = (
        ('Main', {
            'classes': ('full-width',),
            'fields': ('title', 'body',)
        }),

        ('Featured Options (Front Page)', {
            'fields': ('featured_picture', 'featured_text', 'featured_button', 'sticky')
        }),
        ('Extras', {
            'fields': ('listing_picture', 'tags', 'category', 'publish',)
        }),
        ('Advanced options', {
            'fields': ('slug', 'published')
        }),
    )


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(Category)
