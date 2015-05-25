# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User


def same_account(details, user=None, *args, **kwargs):
    """
    Если пользователь с таким email уже существует, то создается только
    объект связывающий существующий аккаунт с входом через соц.сеть
    """
    try:
        user = User.objects.get(email=details['email'])
        user.is_active = True
        user.save()
    except User.DoesNotExist:
        pass
    return {'user': user}


def get_username(details, user=None, *args, **kwargs):
    """
    Возвращает имя пользователя на основе учётной записи в соц.сети,
    чтобы определить зарегистрирован ли у нас такой пользователь.
    """
    return {
        'username': (details['email'],),
    }


def create_user(details, user=None, *args, **kwargs):
    """
    При необходимости создает учётку пользователя и заполняет
    начальными данными полученными от соц.сети.
    """
    if user:
        return {'is_new': False}

    user = User.objects.create_user(details['email'], is_active=True)

    return {
        'is_new': True,
        'user': user,
    }
