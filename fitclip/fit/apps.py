from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FitConfig(AppConfig):
    name = 'fitclip.fit'
    verbose_name = _('치수 데이터 관리')
