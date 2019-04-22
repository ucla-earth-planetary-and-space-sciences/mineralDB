from django.contrib import admin
from main.models import FlatPageEditGroup,StaticLinks,SeminarLinks,Banner
from solo.admin import SingletonModelAdmin
from image_cropping.admin import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin
from django import forms
from django.contrib.flatpages.forms import FlatpageForm as FlatPageFormOld
from django.contrib.flatpages.models import FlatPage
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class FlatPageForm(FlatPageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FlatPage
        fields = ('title', 'content', 'url', 'template_name','sites')


class FlatPageCustomAdmin(admin.ModelAdmin):
    # exclude = ('enable_comments')
    # this cluster F is supposed to control access to flatpages for non superusers.
    def get_queryset(self, request):
        current_groups_list = request.user.groups.values_list('name', flat=True)

        if request.user.is_superuser:
            return super(FlatPageCustomAdmin, self).get_queryset(request)

        # to use this is feature the user has to be in an auth group called "SpecialAdmin" which has no priveleges.
        # I didnt want to override the actual auth classes, so here we are.
        # add the user to special admin, and then the membership to a certain FlatPageEditGroup
        # will filter aceess to flatpages based on this groups members (both pages and users)
        # In this way, we can controll who has access to what flatpages, atomically.
        if u'SpecialAdmin' in current_groups_list:
            page_list = []
            groups = FlatPageEditGroup.objects.all()
            for group in groups:
                members = group.members.values_list('id', flat=True)
                for member in members:
                    if member == request.user.id:
                        g = group.page.values_list(flat=True)
                        for i in g:
                            page_list.append(int(i))
                    else:
                        pass

            return FlatPage.objects.all().filter(id__in=page_list)

    form = FlatPageForm
    list_display = ('url', 'title',)
    search_fields = ('url', 'title')

class SpecialAccessGroups(admin.ModelAdmin):
    pass


class SeminarLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    prepopulated_field = {'slug': ('name',)}


class BannerAdmin(ImageCroppingMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title_text', 'enable_banner')
    list_filter = ['enable_banner']


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustomAdmin)
admin.site.register(FlatPageEditGroup, SpecialAccessGroups)
admin.site.register(StaticLinks, SingletonModelAdmin)
admin.site.register(SeminarLinks, SeminarLinksAdmin)
admin.site.register(Banner, BannerAdmin)
