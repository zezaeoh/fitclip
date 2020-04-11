from django.db import models
from django.utils.translation import ugettext_lazy as _

from fitclip.fit.models.fit_spec import FitSpec, FitSpecOption
from fitclip.fit.models.personal_fit import PersonalFit, PersonalFitUIOption
from fitclip.mall.models.category import Section


class Sub(models.Model):
    name = models.CharField(
        max_length=10,
        verbose_name=_("특징 분류 이름"),
        help_text=_("상세 분류내의 특징적인 분류 이름입니다.")
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name=_("상세 분류")
    )
    fit_specs = models.ManyToManyField(
        FitSpec,
        through=FitSpecOption,
        verbose_name=_("특징 치수 데이터 모음"),
        help_text=_("입력 받아야 할 특징 치수 데이터들의 모음입니다.")
    )
    personal_fits = models.ManyToManyField(
        PersonalFit,
        through=PersonalFitUIOption,
        verbose_name=_("특징 치수 개인화 데이터 모음"),
        help_text=_("입력 받아야 할 특징 치수의 개인화 데이터들의 모음입니다.")
    )

    def category(self) -> str:
        return self.section.category.name
    category.short_description = '카테고리'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = _('특징 분류')
        verbose_name_plural = _('특징 분류')
