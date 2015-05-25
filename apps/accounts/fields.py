# -*- coding: utf-8 -*-
import uuid

from django.db import models


class UUIDField(models.CharField):
    """
    Поле генерирующее секретный ключ
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 64)
        super(UUIDField, self).__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        if add:
            value = str(uuid.uuid4())
            setattr(instance, self.attname, value)
            return value
        else:
            return super(UUIDField, self).pre_save(instance, add)

    def get_internal_type(self):
        return 'CharField'
