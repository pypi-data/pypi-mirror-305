# -*- coding: UTF-8 -*-
__author__ = "yuyang"

import uuid
import time
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class AdminUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(username=username, email=email)
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


from xy_django_model.model import gen_upload_to


@gen_upload_to
def user__thumbnails(instance=None, filename=None):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    pass


class AdminUser(AbstractBaseUser, PermissionsMixin):
    date_of_birth = models.DateTimeField(
        verbose_name=_("生日"),
        auto_now=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("是否启用"),
        default=True,
    )
    is_admin = models.BooleanField(
        verbose_name=_("是否是管理员"),
        default=False,
    )

    objects = AdminUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    # 性别选择
    sex_choices = (
        ("man", _("男")),
        ("female", _("女")),
        ("unknown", _("未知")),
    )
    # 必须
    email = models.EmailField(
        verbose_name=_("邮箱"),
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_("用户名"),
        max_length=255,
        default="",
        blank=False,
        unique=True,
    )
    sex = models.CharField(
        verbose_name=_("性别"),
        default="man",
        choices=sex_choices,
        blank=True,
        max_length=15,
    )
    thumb = models.ImageField(
        verbose_name=_("头像"),
        upload_to=user__thumbnails,
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        verbose_name=_("年龄"),
        default=0,
        blank=True,
        null=True,
    )
    expires_time = models.DateTimeField(
        verbose_name=_("登陆过期时间"),
        auto_now_add=True,
        blank=True,
        null=True,
    )
    nickname = models.CharField(
        verbose_name=_("昵称"),
        max_length=255,
        default="",
        blank=True,
    )
    userid = models.CharField(
        verbose_name=_("用户ID"),
        max_length=100,
        default=str(
            uuid.uuid3(uuid.uuid4(), str(time.time())).hex,
        ),
        blank=True,
        unique=True,
    )

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __iter__(self):
        pass

    class Meta:
        abstract = True
        verbose_name = _("用户")
        verbose_name_plural = _("用户")

    def __str__(self):
        return f"{self.id}. {self.username}"
