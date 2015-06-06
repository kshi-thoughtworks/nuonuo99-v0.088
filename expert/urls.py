#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from expert import views


urlpatterns = (
    url(r'^(\w+)$', views.expert_home, name='expert_home'),
)
