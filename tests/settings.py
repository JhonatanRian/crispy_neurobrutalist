"""
Django settings for running tests.
"""

SECRET_KEY = "test-secret-key-for-crispy-neurobrutalist"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "crispy_forms",
    "crispy_neurobrutalist",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "neobrutalist"
CRISPY_TEMPLATE_PACK = "neobrutalist"

# Templates
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
            ],
        },
    },
]

USE_TZ = True
