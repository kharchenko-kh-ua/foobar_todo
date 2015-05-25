# -*- coding: utf-8 -*-
from django.shortcuts import render

from apps.organizer.models import TodoList


def index(request):
    context = {}
    if request.user.is_authenticated():
        todo_lists = TodoList.objects.filter(owner=request.user)
        context['todo_lists'] = todo_lists
    return render(request, 'index.html', context)
