from . import *


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

INTERNAL_IPS = (
    'localhost',
)

DEVELOPMENT_APPS = (
    'django_extensions',
    'debug_toolbar',
)

INSTALLED_APPS = INSTALLED_APPS + DEVELOPMENT_APPS
