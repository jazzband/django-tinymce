from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include, url

import tinymce.urls

admin.autodiscover()

urlpatterns = [
    url(r'^tinymce/', include(tinymce.urls)),
    url(r'^admin/', admin.site.urls),
    #url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
    #    'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
