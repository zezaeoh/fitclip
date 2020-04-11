from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FitStore(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="fits",
        verbose_name=_("사용자")
    )
    product_name = models.CharField(
        max_length=20,
        verbose_name=_("제품 이름"),
        help_text=_("사용자가 입력한 제품 이름")
    )
    product_img = models.ImageField(
        verbose_name=_("제품 사진"),
        help_text=_("사용자가 첨부한 제품의 사진")
    )
    sub = models.OneToOneField(
        "mall.Sub",
        on_delete=models.CASCADE,
        verbose_name=_("특징 분류")
    )
    raw_fit_specs = models.TextField(
        verbose_name=_('raw 치수 데이터'),
        help_text=_("사용자가 입력한 raw 한 치수 데이터")
    )

    def __str__(self):
        return f'{self.user.get_full_name()} 의 {self.sub.name} 치수 데이터'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('입력 받은 치수 데이터')
        verbose_name_plural = _('입력 받은 치수 데이터들')
