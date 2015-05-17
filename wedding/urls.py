#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('shop.views',
    url(r'^add/(\w+_\d+)$', 'add', name='add_to_cart'),
    url(r'^my$', 'overview', name='wedding_overview'),
)
