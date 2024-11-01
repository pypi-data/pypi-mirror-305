<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_django_app_account/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_account

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

后台账户数据模型.

## 源码仓库

- <a href="https://github.com/xy-django-app/xy_django_app_account.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_account.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_django_app_account
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
    "xy_django_app_account",
    "Demo",
    "Resource",
    "Media",
]

AUTH_USER_MODEL = "xy_django_app_account.AdminUser"
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户系统
```

- ###### 2. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```

##### 2. 自定义

- ###### 1. 创建Account模块

> 操作 [样例工程](./samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Account
# Account 模块创建在 source/Runner/Admin/Account 
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
    "Account",
]

AUTH_USER_MODEL = "Account.AdminUser"
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户系统
```

- ###### 3. 在[Account](./samples/xy_web_server_demo/source/Runner/Admin/Account)模块的[models.py](./samples/xy_web_server_demo/source/Runner/Admin/Account/models.py)文件中加入如下代码

```python
# models.py
from django.utils.translation import gettext_lazy as _

# Create your models here.
from xy_django_app_account.abstracts import (
    AdminUserManager as xyAdminUserManager,
    MAAdminUser as xyAdminUser,
)


class MAdminUserManager(xyAdminUserManager):
    pass


class MAdminUser(xyAdminUser):
    objects = MAdminUserManager()

    class Meta:
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
        app_label = "Account"

```

- ###### 4. 在[Account](./samples/xy_web_server_demo/source/Runner/Admin/Account)模块的[admin.py](./samples/xy_web_server_demo/source/Runner/Admin/Account/admin.py)文件中加入如下代码

```python
# admin.py
from django.contrib import admin

# Register your models here.
from .models import MAdminUser
from xy_django_app_account.aabstracts import *


class AUserCreationForm(AAUserCreationForm):

    class Meta:
        model = MAdminUser
        fields = ("username",)


class AUserChangeForm(AAUserChangeForm):

    class Meta:
        model = MAdminUser
        fields = (
            "password",
            "email",
            "username",
            "is_active",
            "is_admin",
            "sex",
            "thumb",
            "age",
            "userid",
        )


@admin.register(MAdminUser)
class AAdminUserAdmin(AAAdminUserAdmin):
    # The forms to add and change user instances
    form = AAUserChangeForm
    add_form = AAUserCreationForm

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
xy_django_app_account 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)

## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```