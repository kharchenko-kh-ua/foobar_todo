# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


template_name = lambda s: {'template_name': 'accounts/{0}.html'.format(s)}

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^confirm-register/$', views.confirm_register,
        name='confirm_register'),
    url(r'^confirm-register/(?P<secret_key>.+)/$', views.confirm_register,
        name='confirm_register'),
    url(r'^login/$', login, template_name('login'), name='login'),
    url(r'^logout/$', logout, template_name('logged_out'), name='logout'),
]
