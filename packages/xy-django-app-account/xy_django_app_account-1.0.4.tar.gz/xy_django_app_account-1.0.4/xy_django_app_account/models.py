# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "abstracts"
"""
  * @File    :   abstracts.py
  * @Time    :   2024/11/01 09:16:18
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from .abstracts import _, MAAdminUser


class MAdminUser(MAAdminUser):

    class Meta:
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
        app_label = "xy_django_app_account"
