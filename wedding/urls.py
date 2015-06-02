#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('wedding.views',
    url(r'^diy$', 'diy', name='diy_home'),

    url(r'^add-service/mc/(\d+)$', 'add_service_mc', name='add_service_mc'),
    url(r'^add-service/makeup/(\d+)$', 'add_service_makeup', name='add_service_makeup'),
    url(r'^add-service/photo/(\d+)$', 'add_service_photo', name='add_service_photo'),
    url(r'^add-service/vedio/(\d+)$', 'add_service_vedio', name='add_service_vedio'),

    url(r'^add-product/flower/(\d+)/(\d+)$', 'add_product_flower', name='add_product_flower'),

    url(r'^my$', 'diy', name='wedding_overview'),

    url(r'^book/(.*)/(.+)$', 'book', name='book_service'),
)
