from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name=_("대분류 이름"),
        help_text=_("제품을 분류할 카테고리 이름입니다.")
    )
    icon_img = models.ImageField(
        default="/image/category/default.png",
        verbose_name=_("대분류 이미지"),
        help_text=_("카테고리를 표현할 간단한 이미지입니다.")
    )

    @property
    def sections(self):
        return self.section_set

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('카테고리')
        verbose_name_plural = _('카테고리')
