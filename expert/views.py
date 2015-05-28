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
from base.choices import MC_PARAS


def range_filter(name, value):
    kwargs = dict()

    if not value:
        return kwargs

    bottom, top = value.split('-')

    if bottom:
        kwargs['%s__gte' % name] = bottom

    if top:
        kwargs['%s__lte' % name] = top

    return kwargs


def price_action(queryset, value):
    kwargs = range_filter('price', value)
    return queryset.filter(**kwargs)


class McFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(action=price_action)

    class Meta:
        model = MC
        fields = ['wed_sty', 'is_man', 'loc_native', 'price']


def mc_home(request):
    content = {
        'paras': MC_PARAS(),
        }
    return render_to_response('mc.html', RequestContext(request, content))


class McList(generics.ListCreateAPIView):
    queryset = MC.objects.all()
    serializer_class = McSerializer
    filter_class = McFilter


class MakeUpList(generics.ListCreateAPIView):
    queryset = MakeUp.objects.all()
    serializer_class = MakeUpSerializer
