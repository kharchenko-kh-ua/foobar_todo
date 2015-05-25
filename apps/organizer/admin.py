# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TodoList, Entry


class EntriesInline(admin.StackedInline):
    model = Entry
    extra = 1


class TodoListAdmin(admin.ModelAdmin):
    inlines = [EntriesInline]


admin.site.register(TodoList, TodoListAdmin)
