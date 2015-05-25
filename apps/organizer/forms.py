# -*- coding: utf-8 -*-
from django import forms

from .models import TodoList, Entry


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name',)


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
