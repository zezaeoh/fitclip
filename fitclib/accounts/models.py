from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("사용자")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("설명"),
        help_text=_("사용자의 추가적인 정보를 저장합니다.")
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        verbose_name=_("거주 지역"),
        help_text=_("사용자가 거주하는 지역 정보입니다.")
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("가입 날짜")
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        verbose_name=_("최근 정보 변경 날짜")
    )
    is_organizer = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('사용자 정보')
        verbose_name_plural = _('사용자 정보')

    def __str__(self):
        return self.user.username

    def display_location(self) -> str:
        if not self.location:
            return "아직 등록되지 않음"
        return self.location
    display_location.short_description = '거주 지역'
