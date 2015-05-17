#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from expert.models import MC, MakeUp

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def price_filter(query_set):
    kwargs = dict()
    bottom, top = query_set.get('price', '-').split('-')

    if bottom:
        kwargs['price__gte'] = bottom

    if top:
        kwargs['price__lte'] = top

    return kwargs


def expert_filter(query_set):
    kwargs = price_filter(query_set)

    def add_para(db, para):
        value = query_set.get(para, '0')
        if value != '0':
            kwargs[db] = value

    add_para('gender', 'gender')
    add_para('wed_style', 'wed_style')
    add_para('t_birth_age', 'age')

    return kwargs


def filter_mc(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MC.objects.filter(**kwargs),
            }
    return render_to_response('mc.html', RequestContext(request, content))


def filter_makeup(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MakeUp.objects.filter(**kwargs),
            }
    return render_to_response('makeup.html', RequestContext(request, content))
