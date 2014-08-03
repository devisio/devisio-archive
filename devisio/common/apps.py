from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'devisio.common'
    verbose_name = 'common'

    def ready(self):
        from devisio.common import signals
