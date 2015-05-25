# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .tasks import send_confirmation_email
from .models import User, AccountConfirmation


@receiver(pre_save, sender=User, dispatch_uid='accounts:user_pre_save')
def on_user_pre_save(sender, instance=None, **kwargs):
    if instance:
        if instance.is_staff:
            instance.is_active = True


@receiver(post_save, sender=User, dispatch_uid='accounts:user_post_save')
def on_user_post_save(sender, instance, **kwargs):
    if instance and instance.pk:
        if not instance.is_active:
            user = User.objects.get(id=instance.pk)
            confirmation = AccountConfirmation.objects.create(user=user)
            send_confirmation_email.delay(
                settings.PROJECT_HOST, user.email, confirmation)
