# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import User, AccountConfirmation


class AccountsTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'example@mail.com',
            'pass': '123'
        }

    def test_create_user(self):
        self.client.get('/accounts/register/')
        response = self.client.post(
            '/accounts/register/', {
                'email': self.credentials['email'],
                'password1': self.credentials['pass'],
                'password2': self.credentials['pass'],
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn('confirm_register', self.client.session)
        user = User.objects.get(email=self.credentials.get('email'))
        self.assertEqual(user.is_active, False)

        acc_confirmation = AccountConfirmation.objects.get(
            user=user
        )
        response1 = self.client.get(
            reverse('accounts:confirm_register', kwargs={
                'secret_key': acc_confirmation.secret_key
            })
        )
        self.assertIn('Congratulations!', response1.content)
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.get(
            reverse('accounts:login')
        )
        self.assertEqual(response2.status_code, 200)

        response3 = self.client.post(
            '/accounts/login/', {
                'username': self.credentials['email'],
                'password': self.credentials['pass']
            }
        )
        self.assertEqual(response3.status_code, 302)
        self.assertIn('You logged in as {0}'.format(
            self.credentials['email']), self.client.get('/').content)
