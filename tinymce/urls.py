# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from . import views

try:
    from django.conf.urls import url
except:
    try:
        from django.conf.urls.defaults import url
    except ImportError:
        try:
            from django.conf.urls import url
        except ImportError:
            from django.urls import re_path as url

urlpatterns = [
    url(r'^js/textareas/(?P<name>.+)/$', views.textareas_js, name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', views.textareas_js, name='tinymce-js-lang'),
    url(r'^spellchecker/$', views.spell_check),
    url(r'^flatpages_link_list/$', views.flatpages_link_list),
    url(r'^compressor/$', views.compressor, name='tinymce-compressor'),
    url(r'^filebrowser/$', views.filebrowser, name='tinymce-filebrowser'),
    url(r'^preview/(?P<name>.+)/$', views.preview, name='tinymce-preview'),
]
