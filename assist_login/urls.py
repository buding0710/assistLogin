#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 14:55
# @Author  : buding
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/$', views.add),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete),
    url(r'^login/$', views.login),
]