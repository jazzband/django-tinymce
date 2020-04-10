# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

"""
This TinyMCE widget was copied and extended from this code by John D'Agostino:
http://code.djangoproject.com/wiki/CustomWidgetsTinyMCE
"""
from collections import OrderedDict
import json

from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _

import tinymce.settings

try:
    from django.urls import reverse
except ImportError:
    # Django < 1.10
    from django.core.urlresolvers import reverse


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
        mce_attrs = mce_attrs or {}
        self.mce_attrs = mce_attrs
        if "mode" not in self.mce_attrs:
            self.mce_attrs["mode"] = "exact"
        self.mce_attrs["strict_loading_mode"] = 1
        if content_language is None:
            content_language = mce_attrs.get("language", None)
        self.content_language = content_language

    def use_required_attribute(self, *args):
        # The html required attribute may disturb client-side browser validation.
        return False

    def get_mce_config(self, attrs):
        mce_config = tinymce.settings.DEFAULT_CONFIG.copy()
        mce_config.update(get_language_config(self.content_language))
        if tinymce.settings.USE_FILEBROWSER:
            mce_config["file_browser_callback"] = "djangoFileBrowser"
        mce_config.update(self.mce_attrs)
        if mce_config["mode"] == "exact":
            mce_config["elements"] = attrs["id"]
        return mce_config

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        value = force_text(value)
        final_attrs = self.build_attrs(self.attrs, attrs)
        final_attrs["name"] = name
        if final_attrs.get("class", None) is None:
            final_attrs["class"] = "tinymce"
        else:
            final_attrs["class"] = " ".join(final_attrs["class"].split(" ") + ["tinymce"])
        assert "id" in final_attrs, "TinyMCE widget attributes must contain 'id'"
        mce_config = self.get_mce_config(final_attrs)
        mce_json = json.dumps(mce_config)
        if tinymce.settings.USE_COMPRESSOR:
            compressor_config = {
                "plugins": mce_config.get("plugins", ""),
                "themes": mce_config.get("theme", "advanced"),
                "languages": mce_config.get("language", ""),
                "diskcache": True,
                "debug": False,
            }
            final_attrs["data-mce-gz-conf"] = json.dumps(compressor_config)
        final_attrs["data-mce-conf"] = mce_json
        html = [f"<textarea{flatatt(final_attrs)}>{escape(value)}</textarea>"]
        return mark_safe("\n".join(html))

    def _media(self):
        css = None
        if tinymce.settings.USE_COMPRESSOR:
            js = [reverse("tinymce-compressor")]
        else:
            js = [tinymce.settings.JS_URL]
        if tinymce.settings.USE_FILEBROWSER:
            js.append(reverse("tinymce-filebrowser"))
        if tinymce.settings.USE_EXTRA_MEDIA:
            if "js" in tinymce.settings.USE_EXTRA_MEDIA:
                js += tinymce.settings.USE_EXTRA_MEDIA["js"]

            if "css" in tinymce.settings.USE_EXTRA_MEDIA:
                css = tinymce.settings.USE_EXTRA_MEDIA["css"]
        if tinymce.settings.INCLUDE_JQUERY:
            js.append("django_tinymce/jquery-1.9.1.min.js")
        js.append("django_tinymce/init_tinymce.js")
        return forms.Media(css=css, js=js)

    media = property(_media)


class AdminTinyMCE(TinyMCE, admin_widgets.AdminTextareaWidget):
    pass


def get_language_config(content_language=None):
    language = get_language()
    language = language[:2] if language is not None else "en"
    if content_language:
        content_language = content_language[:2]
    else:
        content_language = language

    config = {}
    config["language"] = language

    lang_names = OrderedDict()
    for lang, name in settings.LANGUAGES:
        if lang[:2] not in lang_names:
            lang_names[lang[:2]] = []
        lang_names[lang[:2]].append(_(name))
    sp_langs = []
    for lang, names in lang_names.items():
        if lang == content_language:
            default = "+"
        else:
            default = ""
        sp_langs.append(f'{default}{" / ".join(names)}={lang}')

    config["spellchecker_languages"] = ",".join(sp_langs)

    if content_language in settings.LANGUAGES_BIDI:
        config["directionality"] = "rtl"
    else:
        config["directionality"] = "ltr"

    if tinymce.settings.USE_SPELLCHECKER:
        config["spellchecker_rpc_url"] = reverse("tinymce-spellcheck")

    return config
