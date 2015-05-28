#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

# REST framework
from rest_framework import generics
from rest_framework import permissions

import django_filters

from expert.models import MC, MakeUp
from expert.serializers import McSerializer, MakeUpSerializer

from base.utils import price_filter
import base.choices as choice_set


class McFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=choice_set.range_action('price'))
    age = django_filters.CharFilter(action=choice_set.range_action('t_birth'))
    height = django_filters.CharFilter(action=choice_set.range_action('height'))
    mc_tech = django_filters.CharFilter(lookup_type='isnull')

    class Meta:
        model = MC
        fields = ['price', 'wed_sty', 'is_man', 'age', 'height', 'loc_native', 'mc_tech']


def mc_home(request):
    content = {
        'paras': choice_set.MC_PARAS(),
        }
    return render_to_response('mc.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer
    filter_class = McFilter


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer
