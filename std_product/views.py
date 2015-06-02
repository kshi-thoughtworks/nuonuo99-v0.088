#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions

import django_filters

from std_product.models import WedFlower, WedAv, StageEffect
from std_product.serializers import WedFlowerSerializer, WedAvSerializer, StageEffectSerializer
from std_product.filters import WedFlowerFilter, WedAvFilter, StageEffectFilter

from base.utils import price_filter
import base.choices as choice_set


def wedflower_home(request, cate):
    content = {
        'paras': choice_set.FLOWER_PARAS(cate),
        'list_url': 'flower_list',
        'cart_url': 'add_product_flower',
        'data_set': WedFlower.objects.filter(category=cate),
        'disp_name': choice_set.get_disp_flower_cate(cate),
        'cate': cate,
        }
    return render_to_response('std_product.html', RequestContext(request, content))


class WedFlowerList(generics.ListCreateAPIView):
    queryset = WedFlower.objects.all()
    serializer_class = WedFlowerSerializer
    filter_class = WedFlowerFilter


def wedav_home(request, cate):
    content = {
        'paras': choice_set.AV_PARAS(cate),
        'list_url': 'av_list',
        'cart_url': 'add_product_av',
        'data_set': WedAv.objects.filter(category=cate),
        'disp_name': choice_set.get_disp_av_cate(cate),
        'cate': cate,
        }
    return render_to_response('std_product.html', RequestContext(request, content))


class WedAvList(generics.ListCreateAPIView):
    queryset = WedAv.objects.all()
    serializer_class = WedAvSerializer
    filter_class = WedAvFilter


def stage_home(request, cate):
    content = {
        'paras': choice_set.STAGE_PARAS(cate),
        'list_url': 'stage_list',
        'cart_url': 'add_product_stage',
        'data_set': StageEffect.objects.filter(category=cate),
        'disp_name': choice_set.get_disp_stage_cate(cate),
        'cate': cate,
        }
    return render_to_response('std_product.html', RequestContext(request, content))


class StageEffectList(generics.ListCreateAPIView):
    queryset = StageEffect.objects.all()
    serializer_class = StageEffectSerializer
    filter_class = StageEffectFilter
