from __future__ import absolute_import
from django.conf import settings
from collections import defaultdict
from django.utils.translation import get_language
from django.utils.translation import ugettext as _
from django.utils.datastructures import SortedDict

def get_language_config(content_language=None):
    language = get_language()[:2]
    if content_language is not None:
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
        default = '+' if lang == content_language else ''
        sp_langs.append(u'%s%s=%s' % (default, ' / '.join(names), lang))

    config['spellchecker_languages'] = ','.join(sp_langs)

    if content_language in settings.LANGUAGES_BIDI:
        config['directionality'] = 'rtl'
    else:
        config['directionality'] = 'ltr'

    return config