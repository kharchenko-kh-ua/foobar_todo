# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from django.core.urlresolvers import reverse
from django.conf import settings
from django.template import loader, Context


@shared_task
def send_confirmation_email(domain, user_email, confirmation):
    link_url = 'http://{0}{1}'.format(
        domain,
        reverse('accounts:confirm_register',
                kwargs={'secret_key': confirmation.secret_key}),
    )
    t = loader.get_template('accounts/confirm_register_letter_link.html')
    c = Context({
        'link_url': link_url,
    })
    message = t.render(c)
    subject = 'Confirm register'
    msg = EmailMultiAlternatives(
        subject,
        '',
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    msg.attach_alternative(message, "text/html")
    msg.send()
    return confirmation.save()
