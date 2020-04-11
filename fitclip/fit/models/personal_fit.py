from django.db import models
from django.utils.translation import ugettext_lazy as _


class PersonalFit(models.Model):
    class PersonalFitType(models.TextChoices):
        FLOAT = 'FLT', _('실수형')
        INT = 'INT', _('정수형')

    name = models.CharField(
        max_length=10,
        verbose_name=_("개인화 치수 데이터 이름"),
    )
    personal_fit_type = models.CharField(
        max_length=3,
        choices=PersonalFitType.choices,
        default=PersonalFitType.FLOAT,
        verbose_name=_("개인화 치수 타입"),
        help_text=_("치수 데이터를 입력받을 데이터 타입입니다.")
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('개인화 치수 데이터')
        verbose_name_plural = _('개인화 치수 데이터')


class PersonalFitUIOption(models.Model):
    class PersonalFitUIType(models.TextChoices):
        SLIDE = 'SLD', _('슬라이드')
        BUTTON = 'BTN', _('버튼')

    personal_fit_ui_type = models.CharField(
        max_length=3,
        choices=PersonalFitUIType.choices,
        default=PersonalFitUIType.SLIDE,
        verbose_name=_("개인화 치수 UI 타입"),
        help_text=_("개인화 치수 데이터를 표현 할 UI 타입입니다.")
    )
    group = models.CharField(
        max_length=20,
        verbose_name=_("그룹"),
        help_text=_("그룹으로 묶을 이름입니다."),
    )
    desc = models.CharField(
        max_length=60,
        null=True,
        verbose_name=_("그룹 설명"),
        help_text=_("그룹을 설명합니다."),
    )
    personal_fit = models.ForeignKey(
        PersonalFit,
        on_delete=models.CASCADE,
        verbose_name=_("개인화 치수 데이터")
    )
    sub = models.ForeignKey(
        "mall.Sub",
        on_delete=models.CASCADE,
        verbose_name=_("특징 분류")
    )

    def __str__(self):
        return f"{self.sub.name} 특징 치수 개인화 데이터 {self.personal_fit.name}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('개인화 치수 데이터 UI 옵션')
        verbose_name_plural = _('개인화 치수 데이터 UI 옵션')

