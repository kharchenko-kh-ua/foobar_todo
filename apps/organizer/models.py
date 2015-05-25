# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from apps.accounts.models import User


class TodoList(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, related_name='todo_lists')

    def last_entries(self):
        return self.entries.all()[:5]

    def get_absolute_url(self):
        return reverse('organizer:todo_edit', kwargs={'name': self.name})

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    class Meta:
        ordering = ['sequence_number']

    sequence_number = models.PositiveSmallIntegerField(
        'sequence number', default=1
    )
    todo_list = models.ForeignKey(TodoList, related_name='entries')
    text = models.TextField()
    achieved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            todo_list_entries = Entry.objects.filter(todo_list=self.todo_list)
            if len(todo_list_entries) > 0:
                try:
                    last_entry_seq_number = todo_list_entries.last(
                    ).sequence_number
                    self.sequence_number = last_entry_seq_number + 1
                except Entry.DoesNotExist:
                    self.sequence_number = 1
        super(Entry, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.text