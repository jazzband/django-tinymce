from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
