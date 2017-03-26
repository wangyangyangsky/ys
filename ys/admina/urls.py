# -*- coding: utf-8 -*-

from django.conf.urls import url
from admina import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
]
