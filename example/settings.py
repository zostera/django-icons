import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))

# Include SRC_FOLDER in path
SRC_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "src"))
if SRC_FOLDER not in sys.path:
    sys.path.insert(0, SRC_FOLDER)

SECRET_KEY = "Thank you for using django-icons!"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_icons",
    "tests.app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tests.app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "tests.app.wsgi.application"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

DJANGO_ICONS = {
    "DEFAULTS": {"renderer": "fontawesome", "attrs": {"aria-hidden": True}},
    "RENDERERS": {
        "fontawesome": "FontAwesomeRenderer",
        "bootstrap3": "Bootstrap3Renderer",
        "material": "MaterialRenderer",
        "image": "ImageRenderer",
    },
    "ICONS": {
        "delete": "trash",
        "edit": {"name": "pencil", "title": "Edit"},
        "feather": {"renderer": "tests.app.renderers.CustomSvgRenderer"},
        "paperplane": {"renderer": "tests.app.renderers.CustomSvgRenderer"},
    },
}
