import os
from django.conf import settings
from django.core.exceptions import AppRegistryNotReady

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
                         {'theme': "silver", 'relative_urls': False})

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

INCLUDE_JQUERY = getattr(settings, 'TINYMCE_INCLUDE_JQUERY', True)

USE_EXTRA_MEDIA = getattr(settings, 'TINYMCE_EXTRA_MEDIA', None)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
                          'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL', os.path.join(settings.STATIC_URL, 'tinymce/tinymce.min.js'))
    try:
        from django.contrib.staticfiles import finders
        JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', finders.find('tinymce', all=False))
    except AppRegistryNotReady:
        JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.STATIC_ROOT, 'tinymce'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL', '{!s}js/tinymce/tinymce.min.js'.format(settings.MEDIA_URL))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tinymce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
