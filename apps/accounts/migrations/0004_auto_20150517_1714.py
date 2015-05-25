# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.accounts.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountConfirmation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secret_key', apps.accounts.fields.UUIDField(max_length=64, editable=False)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='is staff'),
        ),
        migrations.AddField(
            model_name='accountconfirmation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
