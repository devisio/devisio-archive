from devisio.settings.base import *


COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False


INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
