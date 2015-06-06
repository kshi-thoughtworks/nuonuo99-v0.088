#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from std_product import views


urlpatterns = (
    url(r'^(\w+)/(\d+)$', views.product_home, name='product_home'),
)
