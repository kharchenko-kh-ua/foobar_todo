# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', 'foobar_todo.views.index', name='index'),
    url(r'^accounts/', include('apps.accounts.urls',
                               app_name='accounts',
                               namespace='accounts'),
        ),
    url(r'organizer/', include('apps.organizer.urls',
                               app_name='organizer',
                               namespace='organizer'),
        ),
]
