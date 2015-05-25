# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import modelformset_factory, inlineformset_factory

from .models import TodoList, Entry
from .forms import TodoForm, EntryForm


def todo_edit(request, name):
    context = {}
    todo = get_object_or_404(TodoList, name=name)
    todo_list_formset = modelformset_factory(
        Entry, fields='__all__', extra=0,
    )
    if request.method == 'POST':
        formset = todo_list_formset(request.POST)
        if formset.is_valid():
            formset.save()
    formset = todo_list_formset(
        initial=[{'todo_list': todo.id}],
        queryset=Entry.objects.filter(todo_list=todo),
    )
    entry_form = EntryForm(
        initial={'todo_list': todo.id}
    )
    entry_form.fields['sequence_number'].widget = forms.HiddenInput()
    entry_form.fields['todo_list'].widget = forms.HiddenInput()
    for form in formset:
        form.fields['todo_list'].widget = forms.HiddenInput()
        form.fields['sequence_number'].widget = forms.HiddenInput(
            attrs={'data-name': 'sequence_number'}
        )
    context['formset'] = formset
    context['todo'] = todo
    context['entry_form'] = entry_form
    return render(request, 'organizer/todo_edit.html', context)


def new_todo(request):
    todo_inline_formset = inlineformset_factory(
        TodoList, Entry, exclude=('sequence_number',)
    )
    if request.method == 'POST':
        todo = TodoForm(request.POST)
        if todo.is_valid():
            instance = todo.save(commit=False)
            instance.owner_id = request.user.id
            instance.save()
            todo_inline = todo_inline_formset(request.POST, instance=instance)
            if todo_inline.is_valid():
                todo_inline.save()
                return redirect('/')
    formset = todo_inline_formset()
    todo = TodoForm()
    context = {
        'form': todo,
        'formset': formset
    }
    return render(request, 'organizer/new_todo.html', context)


def new_entry(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            instance = entry_form.save(commit=False)
            todo_name = instance.todo_list
            instance.save()
            return redirect(
                reverse(
                    'organizer:todo_edit',
                    kwargs={'name': todo_name}
                )
            )
