# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import RegisterForm
from .models import AccountConfirmation


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['confirm_register'] = True
            return HttpResponseRedirect(reverse('accounts:confirm_register'))
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def confirm_register(request, *args, **kwargs):
    if 'secret_key' in kwargs:
        try:
            confirmation = AccountConfirmation.objects.get(
                secret_key=kwargs['secret_key'])
            user = confirmation.user
            user.is_active = True
            user.save()
            confirmation.delete()
            message =\
                'Congratulations!' \
                ' Your account is active now!'
            try:
                del request.session['confirm_register']
            except KeyError:
                pass
            return render(request, 'accounts/confirm_register.html',
                {'message': message})

        except AccountConfirmation.DoesNotExist:
            raise Http404

    if request.session['confirm_register']:
        message = 'The confirm link send to your email'
        return render(request,
                      'accounts/confirm_register.html',
                      {'message': message})
    else:
        return HttpResponseRedirect('/')
