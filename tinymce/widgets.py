"""
This TinyMCE widget was copied and extended from
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE.
"""

from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt
from django.forms.util import smart_unicode
from django.utils.html import escape
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from tinymce.utils import get_language_config

try:
    JS_URL = settings.TINYMCE_JS_URL
except AttributeError:
    JS_URL = settings.MEDIA_URL + 'js/tiny_mce/tiny_mce_src.js'

try:
    DEFAULT_CONFIG = settings.TINYMCE_DEFAULT_CONFIG
except AttributeError:
    DEFAULT_CONFIG = {
        'theme': "simple",
    }

class TinyMCE(forms.Textarea):
    """
    TinyMCE widget. Set settings.TINYMCE_JS_URL to set the location of the
    javascript file. Default is "MEDIA_URL + 'js/tiny_mce/tiny_mce_src.js'".
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

    def __init__(self, content_language=None, attrs=None, mce_attrs={}):
        super(TinyMCE, self).__init__(attrs)
        self.mce_attrs = mce_attrs
        if content_language is None:
            content_language = mce_attrs.get('language', None)
        self.content_language = content_language

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)

        mce_config = DEFAULT_CONFIG.copy()
        mce_config.update(get_language_config(self.content_language))
        mce_config.update(self.mce_attrs)
        mce_config['mode'] = 'exact'
        mce_config['elements'] = final_attrs['id']
        mce_config['spellchecker_rpc_url'] = reverse('tinymce.views.spell_check')
        mce_json = simplejson.dumps(mce_config)

        return mark_safe(
                u'<textarea%s>%s</textarea>'
                u'<script type="text/javascript">tinyMCE.init(%s)</script>'
                    % (flatatt(final_attrs), escape(value), mce_json)
            )

    class Media:
            js = (JS_URL,)
