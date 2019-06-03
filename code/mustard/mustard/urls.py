from django.urls import include, path
from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from collection import views

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.autodiscover()

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('collection/', views.collection_list, name='collection' ),
    path('collection/<int:item>', views.collection_item , name='specimen')
]
