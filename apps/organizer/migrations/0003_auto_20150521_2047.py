# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20150520_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='sequence_number',
        ),
        migrations.AddField(
            model_name='entry',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=b'sequence number'),
            preserve_default=False,
        ),
    ]
