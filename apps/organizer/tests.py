# -*- coding: utf-8 -*-
from django.forms import modelformset_factory
from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse

from apps.accounts.models import User

from .models import Entry, TodoList
from .views import new_entry, new_todo, todo_edit


class OrganizerTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'example@mail.com',
            'pass': '123'
        }
        self.factory = RequestFactory()
        self.user = User.objects.create(
            email=self.credentials.get('email'),
            is_staff=False,
            is_active=True,
            password=self.credentials.get('pass')
        )
        self.user.save()
        self.assertEqual(self.user.is_active, True)
        self.client.login(
            email=self.credentials.get('email'),
            password=self.credentials.get('pass')
        )

    def test_todo_list(self):

        todo_list_name = 'example_todo_list'

        response = self.client.get(reverse('organizer:new_todo'))
        self.assertEqual(response.status_code, 200)

        first_entry_text = 'Do something'
        second_entry_text = 'Do something tomorrow'
        third_entry_text = 'This entry will achieved'
        request = self.factory.post(
            reverse('organizer:new_todo'),
            {
                'name': todo_list_name,
                'entries-0-text': first_entry_text,
                'entries-1-text': second_entry_text,
                'entries-2-text': third_entry_text,
                'entries-2-achieved': 'checked',
                # Management form data
                'entries-TOTAL_FORMS': 3,
                'entries-INITIAL_FORMS': 0,
                'entries-MIN_NUM_FORMS': 0,
                'entries-MAX_NUM_FORMS': 1000,
            })
        request.user = self.user
        response1 = new_todo(request)
        self.assertEqual(response1.status_code, 302)
        test_todo_list = TodoList.objects.get(name=todo_list_name)
        self.assertEqual(len(test_todo_list.entries.all()), 3)

        response2 = self.client.get(
            reverse('organizer:todo_edit', kwargs={'name': todo_list_name})
        )
        self.assertEqual(response2.status_code, 200)
        first_entry = test_todo_list.entries.filter(sequence_number=1)[0]
        self.assertEqual(first_entry.text, first_entry_text)

        changed_entry_text = 'First entry text was changed'

        self.client.post(
            reverse('organizer:todo_edit', kwargs={'name': todo_list_name}),
            {
                'name': todo_list_name,
                'form-0-text': changed_entry_text,
                'form-0-sequence_number': 1,
                'form-0-todo_list': test_todo_list.id,
                'form-0-id': 1,
                'form-1-text': second_entry_text,
                'form-1-sequence_number': 2,
                'form-1-todo_list': test_todo_list.id,
                'form-1-id': 2,
                'form-2-text': third_entry_text,
                'form-2-achieved': 'checked',
                'form-2-sequence_number': 3,
                'form-2-todo_list': test_todo_list.id,
                'form-2-id': 3,
                # Management form data
                'form-TOTAL_FORMS': 3,
                'form-INITIAL_FORMS': 3,
                'form-MIN_NUM_FORMS': 0,
                'form-MAX_NUM_FORMS': 1000,
            }
        )
        self.assertEqual(
            test_todo_list.entries.filter(sequence_number=1)[0].text,
            changed_entry_text
        )

        new_entry_text = 'New entry to exciting todo list'
        self.client.post(
            reverse('organizer:new_entry'),
            {
                'text': new_entry_text,
                'todo_list': test_todo_list.id,
                'sequence_number': 1,  # As default
            }
        )
        exciting_todo_list = TodoList.objects.get(name=todo_list_name)
        self.assertEqual(exciting_todo_list.entries.last().text, new_entry_text)
        self.assertEqual(
            len(exciting_todo_list.entries.all()),
            exciting_todo_list.entries.last().sequence_number,
        )
