from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

import tinymce.urls

urlpatterns = [
    path("tinymce/", include(tinymce.urls)),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
