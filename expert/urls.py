#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from expert import views


urlpatterns = (
    url(r'^mc$', views.mc_home, name='mc_home'),
    url(r'^mc/q$', views.McList.as_view(), name='mc_list'),
    url(r'^makeup$', views.makeup_home, name='makeup_home'),
    url(r'^makeup/q$', views.MakeUpList.as_view(), name='makeup_list'),
    url(r'^photographer$', views.photographer_home, name='photographer_home'),
    url(r'^photographer/q$', views.PhotographerList.as_view(), name='photographer_list'),
    url(r'^vedioguys$', views.vedioguys_home, name='vedioguys_home'),
    url(r'^vedioguys/q$', views.VedioGuysList.as_view(), name='vedioguys_list'),
)
