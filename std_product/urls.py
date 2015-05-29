#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from std_product import views


urlpatterns = (
    url(r'^flower/(\d+)$', views.wedflower_home, name='flower_home'),
    url(r'^flower/q$', views.WedFlowerList.as_view(), name='flower_list'),
)
