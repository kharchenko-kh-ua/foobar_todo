# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, unique=True, max_length=50, verbose_name='email'),
            preserve_default=False,
        ),
    ]
