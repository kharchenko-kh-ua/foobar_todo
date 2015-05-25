# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_auto_20150521_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='sequence_number',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'sequence number'),
        ),
    ]
