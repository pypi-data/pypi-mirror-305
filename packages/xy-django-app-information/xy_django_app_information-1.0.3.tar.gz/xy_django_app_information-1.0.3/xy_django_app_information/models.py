# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "models"
"""
  * @File    :   models.py
  * @Time    :   2023/05/01 20:24:07
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from django.utils.translation import gettext_lazy as _
from .abstracts import *


class MRegion(MARegion):

    class Meta:
        verbose_name = _("地理位置")
        verbose_name_plural = _("地理位置")
        app_label = "xy_django_app_information"


class MVersion(MAVersion):
    versions = models.ManyToManyField(
        "xy_django_app_information.MVersion",
        verbose_name=_("所属版本"),
        related_name="%(app_label)s_%(class)s_versions",
        db_constraint=False,
        blank=True,
    )

    class Meta:
        verbose_name = _("版本")
        verbose_name_plural = _("版本")
        app_label = "xy_django_app_information"


class MDevelopment(MADevelopment):
    version = models.ForeignKey(
        "xy_django_app_information.MVersion",
        verbose_name=_("版本"),
        related_name="%(app_label)s_%(class)s_version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("开发信息")
        verbose_name_plural = _("开发信息")
        app_label = "xy_django_app_information"


class MSystem(MASystem):
    version = models.ForeignKey(
        "xy_django_app_information.MVersion",
        verbose_name=_("版本"),
        related_name="%(app_label)s_%(class)s_version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("区域"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("系统")
        verbose_name_plural = _("系统")
        app_label = "xy_django_app_information"


class MDevice(MADevice):
    system = models.ForeignKey(
        "xy_django_app_information.MSystem",
        verbose_name=_("系统"),
        related_name="%(app_label)s_%(class)s_system",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("设备")
        verbose_name_plural = _("设备")
        app_label = "xy_django_app_information"
