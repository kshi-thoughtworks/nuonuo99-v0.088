#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('std_product.views',
    url(r'^flower/(\w+)$', 'filter_flower', name='flower_filter'),
)
