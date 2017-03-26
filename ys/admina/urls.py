# -*- coding: utf-8 -*-

from django.conf.urls import url
from admina import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^add_news/$', views.add_news),
    url(r'^img/$', views.img),
    url(r'^img_form/$', views.img_form),
]
