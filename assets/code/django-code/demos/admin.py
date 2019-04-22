from django.contrib import admin
from .models import Demonstration
# Register your models here.

class DemoAdmin(admin.ModelAdmin):
    model = Demonstration

    #override save method to make sure youtube embed works.
    def save_model(self, request, obj, form, change):
        obj.video_link = obj.video_link[17:]
        super(DemoAdmin, self).save_model(request, obj, form, change)


admin.site.register(Demonstration,DemoAdmin)