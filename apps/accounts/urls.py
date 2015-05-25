# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

template_name = lambda s: {'template_name': 'accounts/{0}.html'.format(s)}

urlpatterns = patterns(
    'apps.accounts.views',
    url(r'^register/$', 'register', name='register'),
    url(r'^confirm-register/$', 'confirm_register', name='confirm_register'),
    url(r'^confirm-register/(?P<secret_key>.+)/$',
        'confirm_register', name='confirm_register'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', template_name('login'), name='login'),
    url(r'^logout/$', 'logout', template_name('logged_out'), name='logout'),
)