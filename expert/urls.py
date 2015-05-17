#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('expert.views',
    url(r'^mc$', 'filter_mc', name='mc_filter'),
    url(r'^makeup$', 'filter_makeup', name='makeup_filter'),
)
