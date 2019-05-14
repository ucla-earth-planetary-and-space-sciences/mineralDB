from django.urls import path
from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from collection import views


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.autodiscover()

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('collection/', views.collection_list ),
    #path('collection/<pk>', views.collection_detail )


]
