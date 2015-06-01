#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions


from expert.models import MC, MakeUp, Photographer, VedioGuys

from expert.filters import McFilter, MakeUpFilter, PhotographerFilter, VedioGuysFilter
from expert.serializers import McSerializer, MakeUpSerializer, PhotographerSerializer, VedioGuysSerializer

from base.utils import price_filter
import base.choices as choice_set


def mc_home(request):
    data = McFilter(request.GET, queryset=MC.objects.all())

    content = {
        'paras': choice_set.MC_PARAS(),
        'list_url': 'mc_list',
        'cart_url': 'add_service_mc',
        'data_set': data,
        'disp_name': u'司仪',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer
    filter_class = McFilter


def makeup_home(request):
    data = MakeUpFilter(request.GET, queryset=MakeUp.objects.all())

    content = {
        'paras': choice_set.MAKEUP_PARAS(),
        'list_url': 'makeup_list',
        'cart_url': 'add_service_makeup',
        'data_set': data,
        'disp_name': u'化妆师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer
    filter_class = MakeUpFilter


def photographer_home(request):

    data = PhotographerFilter(request.GET, queryset=Photographer.objects.all())

    content = {
        'paras': choice_set.PHOTO_PARAS(),
        'list_url': 'photographer_list',
        'cart_url': 'add_service_mc',
        'data_set': data,
        'disp_name': u'摄影师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class PhotographerList(generics.ListCreateAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
    filter_class = PhotographerFilter


def vedioguys_home(request):

    data = VedioGuysFilter(request.GET, queryset=VedioGuys.objects.all())

    content = {
        'paras': choice_set.VEDIO_PARAS(),
        'list_url': 'vedioguys_list',
        'cart_url': 'add_service_mc',
        'data_set': data,
        'disp_name': u'摄像师',
        }
    return render_to_response('expert.html', RequestContext(request, content))


class VedioGuysList(generics.ListCreateAPIView):
    queryset = VedioGuys.objects.all()
    serializer_class = VedioGuysSerializer
    filter_class = VedioGuysFilter
