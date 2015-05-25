# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('achieved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence_number', models.PositiveSmallIntegerField(verbose_name=b'sequence number')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(related_name='todo_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='todo_list',
            field=models.ForeignKey(to='organizer.TodoList'),
        ),
    ]
