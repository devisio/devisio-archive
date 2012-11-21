from . import *
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default'] =  dj_database_url.config()
