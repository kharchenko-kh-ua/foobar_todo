# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.organizer.views',
    url(r'todo-edit/(?P<name>.+)/$', 'todo_edit', name='todo_edit'),
    url(r'new-todo/$', 'new_todo', name='new_todo'),
    url(r'new-entry/$', 'new_entry', name='new_entry'),
)
