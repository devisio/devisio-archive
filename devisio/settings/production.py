from . import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devisio',
        'USER': 'devisio',
        'PASSWORD': '@8.b3D3&a^/r4,WTM5l4/*6}',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['www.devisio.net', 'devisio.net']

STATIC_URL = 'http://www.devisio.net/static/'

MEDIA_URL = 'http://www.devisio.net/media/'
