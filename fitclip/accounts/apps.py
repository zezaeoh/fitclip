from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'fitclip.accounts'
    verbose_name = _('사용자 관리')

    def ready(self):
        import fitclip.accounts.signals

