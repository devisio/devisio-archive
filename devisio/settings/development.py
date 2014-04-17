from devisio.settings.base import *


COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False


INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


def show_toolbar(request):
    if request.is_ajax():
        return False

    return lambda: bool(settings.DEBUG)


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'devisio.settings.development.show_toolbar'
}
