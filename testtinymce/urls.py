from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('')

if getattr(settings, 'TINYMCE_FILEBROWSER', False):
    urlpatterns += patterns('',
        url(r'^admin/filebrowser/', include('filebrowser.urls')),
    )

urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
        'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)

