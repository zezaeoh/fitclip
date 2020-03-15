from django.db import models
from django.utils.translation import ugettext_lazy as _

# from fitclip.mall.models.category import Sub


class FitSpec(models.Model):
    class FitSpecType(models.TextChoices):
        STRING = 'STR', _('문자열')
        NUMBER = 'NUM', _('숫자')

    name = models.CharField(
        max_length=10,
        verbose_name=_("치수 데이터 이름"),
    )
    fit_spec_type = models.CharField(
        max_length=3,
        choices=FitSpecType.choices,
        default=FitSpecType.STRING,
        verbose_name=_("치수 데이터 타입"),
        help_text=_("치수 데이터를 입력받을 데이터 타입입니다.")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('치수 데이터')
        verbose_name_plural = _('치수 데이터')


class FitSpecOption(models.Model):
    fit_spec = models.ForeignKey(
        FitSpec,
        on_delete=models.CASCADE,
        verbose_name=_("치수 데이터")
    )
    sub = models.ForeignKey(
        "mall.Sub",
        on_delete=models.CASCADE,
        verbose_name=_("특징 분류")
    )
    is_required = models.BooleanField(
        default=False,
        verbose_name=_("필수 입력"),
        help_text=_("필수로 입력 받아야 하는 데이터 일 경우 선택하세요.")
    )

    def __str__(self):
        return f"{self.sub.name} 특징 치수 데이터 {self.fit_spec.name}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('특징 치수 데이터')
        verbose_name_plural = _('특징 치수 데이터')
