# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "abstracts"
"""
  * @File    :   abstracts.py
  * @Time    :   2023/05/01 20:23:13
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid
from xy_django_model.model import gen_upload_to


# Create your models here.
class MARegion(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"),
        max_length=180,
        null=True,
        blank=True,
    )
    language = models.CharField(
        verbose_name=_("语言"),
        max_length=180,
        null=True,
        blank=True,
    )
    region = models.CharField(
        verbose_name=_("地区"),
        max_length=180,
        null=True,
        blank=True,
    )
    region_code = models.CharField(
        verbose_name=_("地区代号"),
        max_length=180,
        null=True,
        blank=True,
    )
    country = models.CharField(
        verbose_name=_("国家"),
        max_length=180,
        null=True,
        blank=True,
    )
    country_code = models.CharField(
        verbose_name=_("国家代号"),
        max_length=180,
        null=True,
        blank=True,
    )
    province = models.CharField(
        verbose_name=_("省份"),
        max_length=180,
        null=True,
        blank=True,
    )
    province_code = models.CharField(
        verbose_name=_("省份代号"),
        max_length=180,
        null=True,
        blank=True,
    )
    city = models.CharField(
        verbose_name=_("城市"),
        max_length=180,
        null=True,
        blank=True,
    )
    address = models.CharField(
        verbose_name=_("地址"),
        max_length=180,
        null=True,
        blank=True,
    )
    town = models.CharField(
        verbose_name=_("镇"),
        max_length=180,
        null=True,
        blank=True,
    )
    district = models.CharField(
        verbose_name=_("区域"),
        max_length=180,
        null=True,
        blank=True,
    )
    full_address = models.CharField(
        verbose_name=_("全部地址"),
        max_length=180,
        null=True,
        blank=True,
    )
    latitude = models.FloatField(
        verbose_name=_("经度"),
        max_length=180,
        null=True,
        blank=True,
    )
    longitude = models.FloatField(
        verbose_name=_("纬度"),
        max_length=180,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("地理位置")
        verbose_name_plural = _("地理位置")

    def __str__(self):
        return f"{self.id}. {self.name} - {self.country} - {self.province} - {self.city} - {self.district}"


@gen_upload_to
def install_package_pack(instance=None, filename=None):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    pass


class MAVersion(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("内部版本名称"),
        max_length=180,
        null=True,
        blank=True,
    )
    detail = models.TextField(
        verbose_name=_("版本介绍"),
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        verbose_name=_("对外版本名称"),
        max_length=180,
        null=True,
        blank=True,
    )
    version_code = models.IntegerField(
        verbose_name=_("版本编码"),
        default=1,
    )
    # Major ：具有相同名称但不同主版本号的程序集不可互换。例如，这适用于对产品的大量重写，这些重写使得无法实现向后兼容性。
    # Minor ：如果两个程序集的名称和主版本号相同，而次版本号不同，这指示显著增强，但照顾到了向后兼容性。例如，这适用于产品的修正版或完全向后兼容的新版本。
    # Build ：内部版本号的不同表示对相同源所作的重新编译。这适合于更改处理器、平台或编译器的情况。
    # Revision ：名称、主版本号和次版本号都相同但修订号不同的程序集应是完全可互换的。这适用于修复以前发布的程序集中的安全漏洞。
    major = models.CharField(
        verbose_name=_("主版本"),
        max_length=180,
        null=False,
        blank=True,
        default="0",
    )
    minor = models.CharField(
        verbose_name=_("次版本"),
        max_length=180,
        null=True,
        blank=True,
    )
    revision = models.CharField(
        verbose_name=_("修正版本"),
        max_length=180,
        null=True,
        blank=True,
    )
    build = models.CharField(
        verbose_name=_("构建版本"),
        max_length=180,
        null=True,
        blank=True,
    )
    create_date = (
        models.DateTimeField(
            verbose_name=_("版本创造日期"),
            null=True,
            blank=True,
        ),
    )
    end_date = models.DateTimeField(
        verbose_name=_("结束支持日期"),
        null=True,
        blank=True,
    )
    lts = models.BooleanField(
        verbose_name=_("长期支持"),
        null=True,
        blank=True,
    )
    force_update = models.BooleanField(
        verbose_name=_("强制更新"),
        null=True,
        blank=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("内部标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )
    version_identifier = models.UUIDField(
        verbose_name=_("外部标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )
    # 性别选择
    version_type_choices = (
        # 正式版
        ("Release", _("最终释放版-Release")),
        ("Registered", _("注册版-Registered")),
        ("Standard", _("标准版-Standard")),
        ("Deluxe", _("豪华版-Deluxe")),
        ("Reference", _("完全版-Reference")),
        ("Professional", _("专业版-Professional")),
        ("Enterprise", _("企业版-Enterprise")),
        # 非正式版
        ("alpha", _("alpha")),
        ("Beta", _("Beta")),
        ("gamma", _("gamma")),
        ("Trial", _("试用版-Trial")),
        ("Unregistered", _("未注册版-Unregistered")),
        ("Demo", _("Demo")),
        # 专有版本
        ("Update", _("更新版-Update")),
        ("OEM", _("OEM版本")),
        ("Stand-Alone", _("单机版本-Stand-Alone")),
        ("Network", _("网络-Network")),
        ("Popular", _("普及版-Popular")),
        ("Hack", _("破解版-Hack")),
    )

    version_type = models.CharField(
        verbose_name=_("版本类型"),
        max_length=180,
        null=True,
        blank=True,
        choices=version_type_choices,
    )
    url = models.URLField(
        verbose_name=_("版本链接"),
        null=True,
        blank=True,
    )
    download_url = models.URLField(
        verbose_name=_("版本下载链接"),
        null=True,
        blank=True,
    )
    install_package = models.FileField(
        verbose_name=_("安装包"),
        upload_to=install_package_pack,
        null=True,
        blank=True,
    )

    debug = False

    @property
    def install_package_url(self):
        if bool(self.install_package) == True:
            protocol = "https"
            if self.debug:
                protocol = "http"
            if hasattr(settings, "PROTOCOL"):
                protocol = settings.PROTOCOL
            return protocol + "://" + settings.DOMAIN + str(self.install_package.url)

        return self.download_url

    class Meta:
        abstract = True
        verbose_name = _("版本")
        verbose_name_plural = _("版本")

    def __str__(self):
        return f"{self.id}. {self.name}"


class MADevelopment(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"),
        max_length=180,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("开发信息")
        verbose_name_plural = _("开发信息")

    def __str__(self):
        return f"{self.id}. {self.name}"


class MASystem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name=_("名称"),
        max_length=180,
        null=True,
        blank=True,
    )
    platform = models.CharField(
        verbose_name=_("平台"),
        max_length=180,
        null=True,
        blank=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("系统")
        verbose_name_plural = _("系统")

    def __str__(self):
        return f"{self.id}. {self.name}"


# Create your models here.
class MADevice(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"),
        max_length=180,
        null=True,
        blank=True,
    )
    model = models.CharField(
        verbose_name=_("设备型号"),
        max_length=180,
        null=True,
        blank=True,
    )
    brand = models.CharField(
        verbose_name=_("品牌"),
        max_length=180,
        null=True,
        blank=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("设备")
        verbose_name_plural = _("设备")

    def __str__(self):
        return f"{self.id}. {self.name}"
