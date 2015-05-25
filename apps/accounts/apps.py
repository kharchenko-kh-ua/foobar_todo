# -*- coding: utf-8 -*-
from django.apps import AppConfig


class AccountsConfig(AppConfig):

    name = 'apps.accounts'
    verbose_name = "Accounts"

    def ready(self):
        import signals
