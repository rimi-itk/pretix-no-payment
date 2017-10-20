from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_nopayment'
    verbose_name = 'No payment'

    class PretixPluginMeta:
        name = ugettext_lazy('No payment')
        author = 'Mikkel Ricky'
        description = ugettext_lazy('Short description')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_nopayment.PluginApp'
