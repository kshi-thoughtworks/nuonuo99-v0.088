#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('wedding.views',
    url(r'^add-service/mc/(\d+)$', 'add_service_mc', name='add_service_mc'),
    url(r'^add-service/makeup/(\d+)$', 'add_service_makeup', name='add_service_makeup'),
    url(r'^my$', 'overview', name='wedding_overview'),
    url(r'^book/(.*)/(.+)$', 'book', name='book_service'),
)
