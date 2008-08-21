from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^js/textareas/(?P<name>.+)/$', 'tinymce.views.textareas_js', name='tinymce-js'),
    #url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', 'tinymce.views.textareas_js', name='tinymce-js'),
    url(r'^spellchecker/$', 'tinymce.views.spell_check'),
)
