# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='todo_list',
            field=models.ForeignKey(related_name='entries', to='organizer.TodoList'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
