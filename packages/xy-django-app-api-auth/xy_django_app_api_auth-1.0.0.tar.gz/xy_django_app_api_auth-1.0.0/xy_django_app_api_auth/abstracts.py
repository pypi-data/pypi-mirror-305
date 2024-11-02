# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "abstracts"
"""
  * @File    :   abstracts.py
  * @Time    :   2024/11/01 08:55:49
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
import time
from django.db import models
from datetime import datetime


# Create your models here.
class MAApiAuthCredential(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=255, null=True, blank=True
    )
    app_key = models.UUIDField(
        verbose_name=_("app_key"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )
    app_secret = models.UUIDField(
        verbose_name=_("app_secret"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("授权用户凭证")
        verbose_name_plural = _("授权用户凭证")

    def __str__(self):
        return str(self.id) + ". " + str(self.name) + " (" + str(self.app_key) + ")"


class MAApiAuthCredentialCache(models.Model):

    id = models.BigAutoField(primary_key=True)

    url = models.TextField(verbose_name=_("名称"), null=True, blank=True)
    time_stamp = models.DateTimeField(
        verbose_name=_("timestamp"), null=True, blank=True
    )
    nonce = models.TextField(verbose_name=_("nonce标识码"), null=True, blank=True)
    sign = models.TextField(verbose_name=_("sign标识码"), null=True, blank=True)

    @property
    def over_time_default(self):
        """超时时间"""
        return 60

    @property
    def time_stamp_validate(self):
        if self.time_stamp == None:
            return False
        return (
            time.mktime(self.time_stamp.timetuple())
            - time.mktime(datetime.now().timetuple())
            <= self.over_time_default
        )

    class Meta:
        abstract = True
        verbose_name = _("授权用户凭证缓存")
        verbose_name_plural = _("授权用户凭证缓存")

    def __str__(self):
        return str(self.id) + ". " + str(self.url)
