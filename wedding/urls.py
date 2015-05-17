#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('wedding.views',
    url(r'^add/(\w+_\d+)$', 'add', name='add_to_cart'),
    url(r'^my$', 'overview', name='wedding_overview'),
    url(r'^charge$', 'charge', name='charge_product'),
)
