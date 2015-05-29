#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions

import django_filters

from std_product.models import WedFlower, WedAv, StageEffect
from std_product.serializers import WedFlowerSerializer, WedAvSerializer, StageEffectSerializer

from base.utils import price_filter
import base.choices as choice_set


class WedFlowerFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))

    class Meta:
        model = WedFlower
        fields = ['price', 'category', 'style']


def wedflower_home(request, cate):
    content = {
        'paras': choice_set.FLOWER_PARAS(cate),
        'list_url': 'flower_list',
        'cart_url': 'add_service_mc',
        'data_set': WedFlower.objects.filter(category=cate),
        'disp_name': choice_set.get_disp_cate(cate),
        }
    return render_to_response('std_product.html', RequestContext(request, content))


class WedFlowerList(generics.ListCreateAPIView):
    queryset = WedFlower.objects.all()
    serializer_class = WedFlowerSerializer
    filter_class = WedFlowerFilter
