import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))

DJANGO_ICONS_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "django_icons"))
if DJANGO_ICONS_FOLDER not in sys.path:
    sys.path.insert(0, DJANGO_ICONS_FOLDER)

DEBUG = True

ADMINS = ()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

TIME_ZONE = "Europe/Amsterdam"

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ""

MEDIA_URL = ""

STATIC_ROOT = ""

STATIC_URL = "/static/"

STATICFILES_DIRS = ("assets",)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

SECRET_KEY = "8s)l4^2s&&0*31-)+6lethmfy3#r1egh^6y^=b9@g!q63r649_"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django_icons",
    "app",
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {"django.request": {"handlers": ["mail_admins"], "level": "ERROR", "propagate": True}},
}

DJANGO_ICONS = {
    "DEFAULTS": {"renderer": "fontawesome4", "attrs": {"aria-hidden": True}},
    "RENDERERS": {
        "fontawesome4": "FontAwesome4Renderer",
        "bootstrap3": "Bootstrap3Renderer",
        "material": "MaterialRenderer",
        "image": "ImageRenderer",
    },
    "ICONS": {
        "delete": "trash",
        "edit": {"name": "pencil", "title": "Edit"},
        "feather": {"renderer": "app.renderers.CustomSvgRenderer"},
        "paperplane": {"renderer": "app.renderers.CustomSvgRenderer"},
    },
}
