from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.views.static import serve

import filebrowser.urls
import tinymce.urls

admin.autodiscover()

urlpatterns = [
    path('admin/filebrowser/', include(filebrowser.urls)),
    path('tinymce/', include(tinymce.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG or settings.ENABLE_MEDIA:
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % getattr(settings, 'MEDIA_URL', '/')[1:], serve,
            {'document_root': getattr(settings, 'MEDIA_ROOT', '/dev/null'),  'show_indexes': True}),
    ]

urlpatterns += staticfiles_urlpatterns()
