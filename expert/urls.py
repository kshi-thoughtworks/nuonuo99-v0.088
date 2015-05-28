#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from expert import views


urlpatterns = (
    url(r'^mc$', views.mc_list, name='mc_list'),
    url(r'^mc/q$', views.McFilter.as_view(), name='mc_filter'),
    url(r'^makeup$', views.MakeUpList.as_view(), name='makeup_list'),
)
