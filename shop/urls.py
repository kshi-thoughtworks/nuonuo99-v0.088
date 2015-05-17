#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('shop.views',
    url(r'^add$', 'add', name='add_to_cart'),
)
