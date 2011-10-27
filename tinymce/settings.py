import os
from django.conf import settings

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
        {'theme': "simple", 'relative_urls': False})

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

JS_URL = getattr(settings, 'TINYMCE_JS_URL', None)
JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', None)

# Always allow overriding of the default settings
if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    if not JS_URL:
        JS_URL = os.path.join(getattr(settings, 'STATIC_URL', ''), 'tiny_mce/tiny_mce.js')
    if not JS_ROOT:
        JS_ROOT = os.path.join(getattr(settings, 'STATIC_ROOT', ''), 'tiny_mce')
else:
    if not JS_URL:
        JS_URL = '%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL
    if not JS_ROOT:
        JS_ROOT = os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce')

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
