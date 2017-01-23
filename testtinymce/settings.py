# Django settings for testtinymce project.

from os.path import join, dirname, realpath

ROOT_PATH = dirname(realpath(__file__))
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_PATH, "testtinymce.sqlite"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
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

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MIDDLEWARE_CLASSES = MIDDLEWARE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
            ]
        },
    },
]

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
    'tinymce',
    'testtinymce.testapp',
)

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "spellchecker",
    'theme_advanced_buttons3_add': "|,spellchecker",
}
