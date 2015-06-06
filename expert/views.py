#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions


from expert.models import mc, makeup, photographer, vedioguys

from expert.filters import mc_filter, makeup_filter, photographer_filter, vedioguys_filter
from expert.serializers import mc_serializer, makeup_serializer, photographer_serializer, vedioguys_serializer

from base.utils import price_filter
import base.choices as choice_set


def mc_home(request):
    data = mc_filter(request.GET, queryset=mc.objects.all())

    content = {
        'paras': choice_set.MC_PARAS(),
        'list_url': 'mc_list',
        'cart_url': 'add_service_mc',
        'data_set': data,
        'disp_name': u'司仪',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = mc.objects.all()
    serializer_class = mc_serializer
    filter_class = mc_filter


def makeup_home(request):
    data = makeup_filter(request.GET, queryset=makeup.objects.all())

    content = {
        'paras': choice_set.MAKEUP_PARAS(),
        'list_url': 'makeup_list',
        'cart_url': 'add_service_makeup',
        'data_set': data,
        'disp_name': u'化妆师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class MakeUpList(generics.ListCreateAPIView):
    queryset = makeup.objects.all()
    serializer_class = makeup_serializer
    filter_class = makeup_filter


def photographer_home(request):

    data = photographer_filter(request.GET, queryset=photographer.objects.all())

    content = {
        'paras': choice_set.PHOTO_PARAS(),
        'list_url': 'photographer_list',
        'cart_url': 'add_service_photo',
        'data_set': data,
        'disp_name': u'摄影师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class PhotographerList(generics.ListCreateAPIView):
    queryset = photographer.objects.all()
    serializer_class = photographer_serializer
    filter_class = photographer_filter


def vedioguys_home(request):

    data = vedioguys_filter(request.GET, queryset=vedioguys.objects.all())

    content = {
        'paras': choice_set.VEDIO_PARAS(),
        'list_url': 'vedioguys_list',
        'cart_url': 'add_service_vedio',
        'data_set': data,
        'disp_name': u'摄像师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class VedioGuysList(generics.ListCreateAPIView):
    queryset = vedioguys.objects.all()
    serializer_class = vedioguys_serializer
    filter_class = vedioguys_filter
