# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "admin"
"""
  * @File    :   admin.py
  * @Time    :   2024/11/01 09:22:09
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from django.contrib import admin
from .aabstracts import AAUserCreationForm, AAUserChangeForm, AAAdminUserAdmin
from .models import MAdminUser


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
