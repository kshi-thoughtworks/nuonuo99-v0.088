#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('service.views',
    url(r'^makeup$', 'filter_makeup', name='makeup_filter'),
)
