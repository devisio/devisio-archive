from . import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'devisio',                      # Or path to database file if using sqlite3.
        'USER': 'devisio',                      # Not used with sqlite3.
        'PASSWORD': '@8.b3D3&a^/r4,WTM5l4/*6}',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS = ['www.devisio.net', 'devisio.net']
