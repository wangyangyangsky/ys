# -*- coding: utf-8 -*-

from django.conf.urls import url
from admina import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^check_news$', views.check_news),
    url(r'^add_admin$', views.add_admin),
    url(r'^check_admin$', views.check_admin),
    url(r'^col_page1$', views.col_page1),
    url(r'^col_page2$', views.col_page2),
    url(r'^img$', views.img),
    url(r'^img_form$', views.img_form),
    #返回界面的函数

    url(r'^create_admin$', views.create_admin),
    url(r'^$', views.login),
    url(r'^inspect_admin$', views.inspect_admin),
    url(r'^create_column$', views.create_column),
    url(r'^inspect_column', views.inspect_column),
    url(r'^delete$', views.delete),
    url(r'^colum_info$', views.colum_info),
    url(r'^add_news_column$', views.add_news_column),
    url(r'^inspect_img$', views.inspect_img),
    url(r'^save_picture$', views.save_picture),
    #有特殊意义的函数
]
