# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0004_auto_20150524_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'sequence number'),
        ),
    ]
