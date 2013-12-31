from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
    #    'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()
