from django.contrib import admin
from django.urls import path, include
from django.contrib.admin import AdminSite

AdminSite.site_title = "EventApp"
AdminSite.site_header = "EventApp"
AdminSite.index_title = "EventApp"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event.urls'))
,]
