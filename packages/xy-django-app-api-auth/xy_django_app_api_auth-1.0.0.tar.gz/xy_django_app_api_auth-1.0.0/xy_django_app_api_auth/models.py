from django.db import models
from django.utils.translation import gettext_lazy as _
from .abstracts import *


class MApiAuthCredential(MAApiAuthCredential):
    versions = models.ManyToManyField(
        "xy_django_app_information.MVersion",
        verbose_name=_("所属版本"),
        related_name="%(app_label)s_%(class)s_versions",
        blank=True,
    )

    class Meta:
        verbose_name = _("授权用户凭证")
        verbose_name_plural = _("授权用户凭证")
        app_label = "xy_django_app_api_auth"


class MApiAuthCredentialCache(MAApiAuthCredentialCache):
    credential = models.ForeignKey(
        "xy_django_app_api_auth.MApiAuthCredential",
        verbose_name=_("凭证"),
        related_name="%(app_label)s_%(class)s_credential",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("授权用户凭证缓存")
        verbose_name_plural = _("授权用户凭证缓存")
        app_label = "xy_django_app_api_auth"
