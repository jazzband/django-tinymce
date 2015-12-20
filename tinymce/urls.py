# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)
from django.conf.urls import url

from tinymce import views

urlpatterns = [
    url(r'^js/textareas/(?P<name>.+)/$', views.textareas_js,
        name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', views.textareas_js,
        name='tinymce-js-lang'),
    url(r'^spellchecker/$', views.spell_check),
    url(r'^flatpages_link_list/$', views.flatpages_link_list),
    url(r'^compressor/$', views.compressor, name='tinymce-compressor'),
    url(r'^filebrowser/$', views.filebrowser, name='tinymce-filebrowser'),
    url(r'^preview/(?P<name>.+)/$', views.preview, name='tinymce-preview'),
]
