# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from django.conf.urls import patterns, include, url

urlpatterns = patterns('tinymce.views',
    url(r'^js/textareas/(?P<name>.+)/$', 'textareas_js', name='tinymce-js'),
    url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', 'textareas_js', name='tinymce-js-lang'),
    url(r'^spellchecker/$', 'spell_check'),
    url(r'^flatpages_link_list/$', 'flatpages_link_list'),
    url(r'^compressor/$', 'compressor', name='tinymce-compressor'),
    url(r'^filebrowser/$', 'filebrowser', name='tinymce-filebrowser'),
    url(r'^preview/(?P<name>.+)/$', 'preview', name='tinymce-preview'),
)
