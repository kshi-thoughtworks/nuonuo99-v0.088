#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('std_product.views',
    url(r'^filter/(\w+)$', 'filter_html', name='expert_filter'),
)
