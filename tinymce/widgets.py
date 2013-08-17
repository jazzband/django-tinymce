# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

"""
This TinyMCE widget was copied and extended from this code by John D'Agostino:
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
"""
from __future__ import unicode_literals

import tinymce.settings
from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt
from django.utils.html import escape
from django.utils.datastructures import SortedDict
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _
try:
    import json
except ImportError:
    from django.utils import simplejson as json
try:
    from django.utils.encoding import smart_text as smart_unicode
except ImportError:
    try:
        from django.utils.encoding import smart_unicode
    except ImportError:
        from django.forms.util import smart_unicode


class TinyMCE(forms.Textarea):
    """
    TinyMCE widget. Set settings.TINYMCE_JS_URL to set the location of the
    javascript file. Default is "MEDIA_URL + 'js/tiny_mce/tiny_mce.js'".
    You can customize the configuration with the mce_attrs argument to the
    constructor.

    In addition to the standard configuration you can set the
    'content_language' parameter. It takes the value of the 'language'
    parameter by default.

    In addition to the default settings from settings.TINYMCE_DEFAULT_CONFIG,
    this widget sets the 'language', 'directionality' and
    'spellchecker_languages' parameters by default. The first is derived from
    the current Django language, the others from the 'content_language'
    parameter.
    """

    def __init__(self, content_language=None, attrs=None, mce_attrs=None):
        super(TinyMCE, self).__init__(attrs)
        if mce_attrs is None:
            mce_attrs = {}
        self.mce_attrs = mce_attrs
        if content_language is None:
            content_language = mce_attrs.get('language', None)
        self.content_language = content_language

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name
        assert 'id' in final_attrs, "TinyMCE widget attributes must contain 'id'"

        mce_config = tinymce.settings.DEFAULT_CONFIG.copy()
        mce_config.update(get_language_config(self.content_language))
        if tinymce.settings.USE_FILEBROWSER:
            mce_config['file_browser_callback'] = "djangoFileBrowser"
        mce_config.update(self.mce_attrs)
        if not 'mode' in mce_config:
            mce_config['mode'] = 'exact'
        if mce_config['mode'] == 'exact':
            mce_config['elements'] = final_attrs['id']
        mce_config['strict_loading_mode'] = 1
        
        # Fix for js functions
        js_functions = {}
        for k in ('paste_preprocess','paste_postprocess'):
            if k in mce_config:
               js_functions[k] = mce_config[k]
               del mce_config[k]
        mce_json = json.dumps(mce_config)

        pos = final_attrs['id'].find('__prefix__')
        if pos != -1:
            mce_json = mce_json.replace('"%s"' % final_attrs['id'], 'elements')

        for k in js_functions:
            index = mce_json.rfind('}')
            mce_json = mce_json[:index]+', '+k+':'+js_functions[k].strip()+mce_json[index:]
            

        html = ['<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        if tinymce.settings.USE_COMPRESSOR:
            compressor_config = {
                'plugins': mce_config.get('plugins', ''),
                'themes': mce_config.get('theme', 'advanced'),
                'languages': mce_config.get('language', ''),
                'diskcache': True,
                'debug': False,
            }
            compressor_json = json.dumps(compressor_config)
            html.append('<script type="text/javascript">tinyMCE_GZ.init(%s)</script>' % compressor_json)
            
        if pos != -1:
            html.append('''<script type="text/javascript">
setTimeout(function () {
    var id = '%s';
    
    if (typeof(window._tinymce_inited) == 'undefined') {
        window._tinymce_inited = [];
    }
    
    if (typeof(window._tinymce_inited[id]) == 'undefined') {
        window._tinymce_inited[id] = true;
    } else {
        var elements = id.replace(/__prefix__/, parseInt(document.getElementById('%sTOTAL_FORMS').value) - 1);
        if (document.getElementById(elements)) {
            tinymce.init(%s);
        }
    }
}, 0);
</script>''' % (final_attrs['id'], final_attrs['id'][0:pos], mce_json))
        else:
            html.append('<script type="text/javascript">tinyMCE.init(%s)</script>' % mce_json)

        return mark_safe('\n'.join(html))

    def _media(self):
        if tinymce.settings.USE_COMPRESSOR:
            js = [reverse('tinymce-compressor')]
        else:
            js = [tinymce.settings.JS_URL]
        if tinymce.settings.USE_FILEBROWSER:
            js.append(reverse('tinymce-filebrowser'))
        return forms.Media(js=js)
    media = property(_media)


class AdminTinyMCE(admin_widgets.AdminTextareaWidget, TinyMCE):
    pass


def get_language_config(content_language=None):
    language = get_language()[:2]
    if content_language:
        content_language = content_language[:2]
    else:
        content_language = language

    config = {}
    config['language'] = language

    lang_names = SortedDict()
    for lang, name in settings.LANGUAGES:
        if lang[:2] not in lang_names: lang_names[lang[:2]] = []
        lang_names[lang[:2]].append(_(name))
    sp_langs = []
    for lang, names in lang_names.items():
        if lang == content_language:
            default = '+'
        else:
            default = ''
        sp_langs.append('%s%s=%s' % (default, ' / '.join(names), lang))

    config['spellchecker_languages'] = ','.join(sp_langs)

    if content_language in settings.LANGUAGES_BIDI:
        config['directionality'] = 'rtl'
    else:
        config['directionality'] = 'ltr'

    if tinymce.settings.USE_SPELLCHECKER:
        config['spellchecker_rpc_url'] = reverse('tinymce.views.spell_check')

    return config
