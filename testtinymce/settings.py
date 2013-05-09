# Django settings for testtinymce project.

from os.path import join, dirname, realpath

ROOT_PATH = dirname(realpath(__file__))
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_PATH, "testtinymce.sqlite"),
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(ROOT_PATH, "media")
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = join(ROOT_PATH, "static")
STATIC_URL = "/static/"

SECRET_KEY = 'w4o4x^&b4h4zne9&3b1m-_p-=+&n_i_sdf@oz=gd+6h6v1$sd9'

ROOT_URLCONF = 'testtinymce.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django_extensions',
    'grappelli',
    'filebrowser',
    'tinymce',
    'testapp',
)

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "spellchecker",
    'theme_advanced_buttons3_add': "|,spellchecker",
}
TINYMCE_DEFAULT_CONFIG = {
    # General options
    'mode' : "textareas",
    'theme' : "advanced",
    'plugins' : "media,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

    'theme_advanced_buttons1_add' : "media",
    'theme_advanced_buttons2_add' : "advimage",

    # Theme options
    'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,", 
    'theme_advanced_buttons2' : "bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,|,forecolor,backcolor",

    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : 'true',

    #Example content CSS (should be your site CSS)
    #content_css : "/css/style.css",

    'template_external_list_url' : "lists/template_list.js",
    'external_link_list_url' : "lists/link_list.js",
    'external_image_list_url' : "lists/image_list.js",
    'media_external_list_url' : "lists/media_list.js",

    # Style formats
    'style_formats' : [
        {'title' : 'Bold text', 'inline' : 'strong'},
        {'title' : 'Red text', 'inline' : 'span', 'styles' : {'color' : '#ff0000'}},
        {'title' : 'Help', 'inline' : 'strong', 'classes' : 'help'},
        {'title' : 'Table styles'},
        {'title' : 'Table row 1', 'selector' : 'tr', 'classes' : 'tablerow'}
    ],

    'width': '700',
    'height': '400'
}
