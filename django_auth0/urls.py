# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import auth_callback, log_out


urlpatterns = [
    url(r'callback/?$', auth_callback, name='auth_callback'),
    url(r'logout/$', log_out, name='log_out'),
]
