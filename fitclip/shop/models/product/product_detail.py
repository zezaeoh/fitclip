from typing import List

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fitclip.shop.models.product import Product


class ProductDetail(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="detail",
        verbose_name=_("제품")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("제품 상세 설명"),
        help_text=_("제품의 디테일 페이지에 표시될 상세 설명입니다.")
    )
    thumbnail = models.ImageField(
        default=staticfiles_storage.url("product/default.png"),
        verbose_name=_("대표 이미지"),
        help_text=_("제품의 대표 이미지입니다.")
    )
    img_1 = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("이미지 01"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_2 = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("이미지 02"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_3 = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("이미지 03"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_4 = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("이미지 04"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_5 = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("이미지 05"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )

    _meta_data = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("메타데이터"),
        help_text=_("json format의 메타데이터입니다.")
    )

    @property
    def size(self) -> List[str]:
        pass

    class Meta:
        verbose_name = _('제품 상세 정보')
        verbose_name_plural = _('제품 상세 정보')