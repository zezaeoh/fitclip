from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import ugettext_lazy as _

from fitclip.shop.models.category import Category, Section
from fitclip.shop.models.shop import Shop


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("제품 이름"),
        help_text=_("제품의 이름입니다.")
    )
    price = models.IntegerField(
        verbose_name=_("제품 가격"),
        help_text=_("제품의 가격입니다.")
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name=_("쇼핑몰")
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("카테고리")
    )
    section = models.ForeignKey(
        Section,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("상세 분류")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    @property
    def repr_img(self) -> ImageFieldFile:
        return self.detail.thumbnail

    class Meta:
        verbose_name = _('제품')
        verbose_name_plural = _('제품')