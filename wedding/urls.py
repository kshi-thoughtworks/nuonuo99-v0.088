#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('wedding.views',
    url(r'^diy$', 'diy', name='diy_home'),

    url(r'^add-service/mc/(\d+)$', 'add_service_mc', name='add_service_mc'),
    url(r'^add-service/makeup/(\d+)$', 'add_service_makeup', name='add_service_makeup'),
    url(r'^add-service/photo/(\d+)$', 'add_service_photo', name='add_service_photographer'),
    url(r'^add-service/vedio/(\d+)$', 'add_service_vedio', name='add_service_vedioguys'),

    url(r'^add-product/flower/(\d+)/(\d+)$', 'add_product_flower', name='add_product_flower'),
    url(r'^add-product/av/(\d+)/(\d+)$', 'add_product_av', name='add_product_av'),
    url(r'^add-product/stage/(\d+)/(\d+)$', 'add_product_stage', name='add_product_stage'),

    url(r'^my$', 'scheme_overview', name='wedding_overview'),

    url(r'^book/(.*)/(.+)$', 'book', name='book_service'),
    url(r'^del/(.+)$', 'delete', name='del_service'),
    url(r'^wedinfo$', 'edit_essential', name='edit_essential'),
    url(r'^set-provider/(\w+)/(\d+)$', 'update_p_wed', name='update_p_wed'),

    url(r'^set-number/(\d+)$', 'update_product', name='update_product'),
    url(r'^set-more/(\d+)$', 'update_expert', name='update_expert'),

    url(r'^buy/(.+)/(\d+)$', 'buy', name='buy'),
)
