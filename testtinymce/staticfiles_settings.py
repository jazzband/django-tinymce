from os.path import join, dirname
from settings import *

CURRENT_PATH = os.getcwd()

INSTALLED_APPS += ('filebrowser', 'staticfiles',)
STATIC_ROOT = join(CURRENT_PATH, "staticfiles")
STATIC_URL = "/media/static/"
MEDIA_ROOT = join(CURRENT_PATH, "media")
MEDIA_URL = "/media/"
TINYMCE_JS_URL = join(STATIC_URL, "tiny_mce", "tiny_mce.js")
ROOT_URLCONF = 'testtinymce.staticfiles_urls'

if DEBUG:
    FILEBROWSER_DEBUG = True
