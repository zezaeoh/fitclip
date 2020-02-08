from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.utils.translation import ugettext_lazy as _

from fitclip.mall.models.category import Category, Section
from fitclip.mall.models.shop import Shop


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("제품 이름"),
        help_text=_("제품의 이름입니다.")
    )
    url = models.URLField(
        null=True,
        verbose_name=_("제품 url"),
        help_text=_("해당 제품으로 넘어가는 링크입니다.")
    )
    price = models.IntegerField(
        verbose_name=_("제품 가격"),
        help_text=_("제품의 가격입니다.")
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        verbose_name=_("쇼핑몰"),
        help_text=_("해당 제품을 판매하는 쇼핑몰입니다.")
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("카테고리"),
        help_text=_("해당 제품의 카테고리입니다.")
    )
    section = models.ForeignKey(
        Section,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("상세 분류"),
        help_text=_("해당 제품의 상세 분류입니다.")
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