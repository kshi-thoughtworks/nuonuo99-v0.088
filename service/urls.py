#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('service.views',
    url(r'^makeup$', 'filter_makeup', name='makeup_filter'),
    url(r'^flower$', 'filter_flower', name='flower_filter'),
)
