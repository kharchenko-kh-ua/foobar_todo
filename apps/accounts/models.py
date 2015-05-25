# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
    PermissionsMixin

from .fields import UUIDField


class UserManager(BaseUserManager):
    def _create_account(self, is_superuser, email, is_active=False,
                        password=None):
        if is_superuser and password is None:
            raise ValueError("Password has been provided")
        user = self.model(
            is_superuser=is_superuser,
            is_staff=is_superuser,
            email=email,
            is_active=is_active,
        )
        user.set_password(password)
        if user.is_superuser:
            user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, *args, **kwargs):
        return self._create_account(False, *args, **kwargs)

    def create_superuser(self, *args, **kwargs):
        return self._create_account(True, *args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField('email', max_length=50, unique=True)
    is_staff = models.BooleanField('is staff', default=False)
    is_active = models.BooleanField('is active', default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email


class AccountConfirmation(models.Model):
    user = models.ForeignKey(User)
    secret_key = UUIDField(editable=False)
    added = models.DateTimeField(
        "creation_date",
        auto_now_add=True
    )
