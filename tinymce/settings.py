import os
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
        {'theme': "modern", 'relative_urls': False})

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

JS_URL = staticfiles_storage.url('tinymce/tinymce.min.js')
JS_ROOT = staticfiles_storage.url('tinymce')

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
