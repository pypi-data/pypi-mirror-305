<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_django_app_api_auth/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_api_auth

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

接口授权模型.

## 源码仓库

- <a href="https://github.com/xy-django-app/xy_django_app_api_auth.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_api_auth.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_django_app_api_auth
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
    "xy_django_app_api_auth",
    "Demo",
    "Resource",
    "Media",
]

```

- ###### 2. 运行项目

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

##### 2. 自定义

- ###### 1. 创建ApiAuth模块

> 操作 [样例工程](./samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp ApiAuth
# ApiAuth 模块创建在 source/Runner/Admin/ApiAuth 
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
    "Demo",
    "Resource",
    "Media",
    "ApiAuth",
]

```

- ###### 3. 在[ApiAuth](./samples/xy_web_server_demo/source/Runner/Admin/ApiAuth)模块的[models.py](./samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/models.py)文件中加入如下代码

```python
# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from xy_django_app_api_auth.abstracts import *


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
        app_label = "ApiAuth"


class MApiAuthCredentialCache(MAApiAuthCredentialCache):
    credential = models.ForeignKey(
        "ApiAuth.MApiAuthCredential",
        verbose_name=_("凭证"),
        related_name="%(app_label)s_%(class)s_credential",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("授权用户凭证缓存")
        verbose_name_plural = _("授权用户凭证缓存")
        app_label = "ApiAuth"

```

- ###### 4. 在[ApiAuth](./samples/xy_web_server_demo/source/Runner/Admin/ApiAuth)模块的[admin.py](./samples/xy_web_server_demo/source/Runner/Admin/ApiAuth/admin.py)文件中加入如下代码

```python
# admin.py
# -*- coding: UTF-8 -*-


from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MApiAuthCredential)
class AApiAuthCredential(admin.ModelAdmin):
    pass


@admin.register(MApiAuthCredentialCache)
class AApiAuthCredentialCache(admin.ModelAdmin):
    pass

```

- ###### 5. 运行项目

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证接口授权管理系统
```

## 许可证
xy_django_app_api_auth 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```