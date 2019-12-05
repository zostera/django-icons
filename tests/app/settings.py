SECRET_KEY = "Thanks for using django-bootstrap4!"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

INSTALLED_APPS = (
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Our tests
    "django_icons",
    "tests",
)

ROOT_URLCONF = "tests.app.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # required for django.contrib.admin
    "django.contrib.messages.middleware.MessageMiddleware",  # required for django.contrib.admin
)

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
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
