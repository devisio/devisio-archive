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

INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
