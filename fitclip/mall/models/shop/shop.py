from django.db import models
from django.utils.translation import ugettext_lazy as _


class Shop(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("쇼핑몰 이름"),
        help_text=_("쇼핑몰의 이름입니다.")
    )
    url = models.URLField(
        null=True,
        verbose_name=_("쇼핑몰 url"),
        help_text=_("쇼핑몰의 링크입니다.")
    )
    logo_img = models.ImageField(
        default="/image/mall/default.png",
        verbose_name=_("쇼핑몰 로고 이미지"),
        help_text=_("쇼핑몰의 대표 이미지입니다.")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('쇼핑몰')
        verbose_name_plural = _('쇼핑몰')
