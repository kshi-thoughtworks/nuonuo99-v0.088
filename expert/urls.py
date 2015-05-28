#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from expert import views


urlpatterns = (
    url(r'^mc$', views.McList.as_view(), name='mc_list'),
    url(r'^makeup$', views.MakeUpList.as_view(), name='makeup_list'),
)
