from __future__ import annotations

import os
import uuid
from typing import List

from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

from fitclip.mall.models.product import Product


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance: ProductDetail, filename: str):
        ext = filename.split('.')[-1]  # eg: 'jpg'
        uid = uuid.uuid4().hex[:10]  # eg: '567ae32f97'

        renamed_filename = f'{instance.product.id}/{uid}.{ext}'
        return os.path.join(self.path, renamed_filename)


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
        default="/image/product/default.png",
        upload_to=PathAndRename('/image/product/'),
        verbose_name=_("대표 이미지"),
        help_text=_("제품의 대표 이미지입니다.")
    )
    img_1 = models.ImageField(
        null=True,
        blank=True,
        upload_to=PathAndRename('/image/product/'),
        verbose_name=_("이미지 01"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_2 = models.ImageField(
        null=True,
        blank=True,
        upload_to=PathAndRename('/image/product/'),
        verbose_name=_("이미지 02"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_3 = models.ImageField(
        null=True,
        blank=True,
        upload_to=PathAndRename('/image/product/'),
        verbose_name=_("이미지 03"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_4 = models.ImageField(
        null=True,
        blank=True,
        upload_to=PathAndRename('/image/product/'),
        verbose_name=_("이미지 04"),
        help_text=_("제품의 디테일 페이지에 표시될 이미지입니다.")
    )
    img_5 = models.ImageField(
        null=True,
        blank=True,
        upload_to=PathAndRename('/image/product/'),
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

    def __str__(self):
        return f"{self.product.name} 상세 정보"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('제품 상세 정보')
        verbose_name_plural = _('제품 상세 정보')