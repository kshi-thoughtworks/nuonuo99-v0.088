#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from expert import views


urlpatterns = (
    url(r'^mc$', views.mc_home, name='mc_home'),
    url(r'^mc/q$', views.McList.as_view(), name='mc_list'),
    url(r'^makeup$', views.MakeUpList.as_view(), name='makeup_list'),
)
