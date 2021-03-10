from os.path import dirname, join, realpath

ROOT_PATH = dirname(realpath(__file__))
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": join(ROOT_PATH, "tests.sqlite"),
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

TIME_ZONE = "America/Chicago"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(ROOT_PATH, "media")
MEDIA_URL = "/media/"
ADMIN_MEDIA_PREFIX = "/static/admin/"

STATICFINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = "/static/"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
MIDDLEWARE_CLASSES = MIDDLEWARE

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

SECRET_KEY = "w4o4x^&b4h4zne9&3b1m-_p-=+&n_i_sdf@oz=gd+6h6v1$sd9"

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.flatpages",
    "tinymce",
    "tests.testapp",
)

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": False,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount",
    "toolbar": "undo redo | formatselect | "
    "bold italic backcolor | alignleft aligncenter "
    "alignright alignjustify | bullist numlist outdent indent | "
    "removeformat | help",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
