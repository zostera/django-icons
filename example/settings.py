import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))

# Include SRC_FOLDER in path
SRC_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "src"))
if SRC_FOLDER not in sys.path:
    sys.path.insert(0, SRC_FOLDER)

DEBUG = True
ADMINS = ()

SECRET_KEY = "Thanks for using django-bootstrap5!"

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

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

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
    "DEFAULTS": {"attrs": {"aria-hidden": True}},
    "ICONS": {
        "delete": {"name": "trash", "title": "Edit", "renderer": "fontawesome4"},
        "feather": {"renderer": "app.renderers.CustomSvgRenderer"},
        "paperplane": {"renderer": "app.renderers.CustomSvgRenderer"},
        "no-pictures-please": {
            "name": "fa-stack",
            "tag": "span",
            "extra_classes": "fa-2x",
            "content": [
                {"name": "fa-solid fa-camera fa-stack-1x"},
                {"name": "fa-solid fa-ban fa-stack-2x", "attrs": {"style": "color:Tomato"}},
            ],
        },
    },
}
