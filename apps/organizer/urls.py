# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'todo-edit/(?P<name>.+)/$', views.todo_edit, name='todo_edit'),
    url(r'new-todo/$', views.new_todo, name='new_todo'),
    url(r'new-entry/$', views.new_entry, name='new_entry'),
]
