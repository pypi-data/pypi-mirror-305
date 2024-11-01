<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_django_app_information/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_information

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

通用信息数据模型.

## 源码仓库

- <a href="https://github.com/xy-django-app/xy_django_app_information.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_information.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_django_app_information
```

## 使用


##### 1. 直接引入

- ###### 1. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](./samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_information",
    "Demo",
    "Resource",
    "Media",
    "Information",
]

```

- ###### 2. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证信息管理系统
```

##### 2. 自定义

- ###### 1. 创建Information模块

> 操作 [样例工程](./samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Information
# Information 模块创建在 source/Runner/Admin/Information 
```

- ###### 2. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](./samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_information",
    "Demo",
    "Resource",
    "Media",
    "Information",
]

```

- ###### 3. 在[Information](./samples/xy_web_server_demo/source/Runner/Admin/Information)模块的[models.py](./samples/xy_web_server_demo/source/Runner/Admin/Information/models.py)文件中加入如下代码

```python
# models.py
from xy_django_app_information.abstracts import MARegion

from django.utils.translation import gettext_lazy as _


class MRegion(MARegion):
    class Meta:
        app_label = "Information"
        verbose_name = _("地理信息")
        verbose_name_plural = _("地理信息")

```

- ###### 4. 在[Information](./samples/xy_web_server_demo/source/Runner/Admin/Information)模块的[admin.py](./samples/xy_web_server_demo/source/Runner/Admin/Information/admin.py)文件中加入如下代码

```python
# admin.py
from django.contrib import admin
from .models import MRegion

# Register your models here.


@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    pass

```

- ###### 5. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```

##### 运行 [样例工程](./samples/xy_web_server_demo)

> 样例工程具体使用方式请移步 <b style="color: blue">xy_web_server.git</b> 下列仓库
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github地址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee地址</a>


## 许可证
xy_django_app_information 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```