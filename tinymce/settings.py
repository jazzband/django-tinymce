import os
import warnings
from django.conf import settings
from django.contrib.staticfiles import finders

OLD_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', False)
if OLD_CONFIG:
    warnings.warn("TINYMCE_DEFAULT_CONFIG is deprecated, check docs for instructions.", DeprecationWarning)
DEFAULT_CONFIG = OLD_CONFIG or {'theme': "modern", 'relative_urls': False}

if getattr(settings, 'TINYMCE_JS_URL', False):
    raise RuntimeError("TINYMCE_JS_URL is not supported anymore, check docs for instructions.")

JS_URL = getattr(settings, 'TINYMCE_JS_URL', os.path.join(settings.STATIC_URL, 'tinymce/tinymce.min.js'))
JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', finders.find('tinymce', all=False))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]

if getattr(settings, 'TINYMCE_SPELLCHECKER', False):
    raise NotImplementedError("TINYMCE_SPELLCHECKER is not implemented yet.")
USE_SPELLCHECKER = False

if getattr(settings, 'TINYMCE_COMPRESSOR', False):
    raise NotImplementedError("TINYMCE_COMPRESSOR is not implemented yet.")
USE_COMPRESSOR = False

# if getattr(settings, 'TINYMCE_FILEBROWSER', False):
#     raise RuntimeError("TINYMCE_FILEBROWSER is not supported anymore, check docs for instructions.")

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', False)