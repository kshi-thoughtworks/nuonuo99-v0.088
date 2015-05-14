#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from service.models import MC, MakeUp, S_Flower

from base.models import C_FLOWER_STYLE_DOOR, C_FLOWER_STYLE_DESK, C_FLOWER_STYLE_ROAD

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def expert_filter(query_set):
    kwargs = dict()

    def add_para(db, para):
        value = query_set.get(para, '0')
        print para, value
        if value != '0':
            kwargs[db] = value

    add_para('gender', 'gender')
    add_para('wed_style', 'wed_style')
    add_para('t_birth_age', 'age')

    return kwargs


def filter_makeup(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MakeUp.objects.filter(**kwargs),
            }
    return render_to_response('makeup.html', RequestContext(request, content))


def filter_mc(request):
    kwargs = expert_filter(request.GET)
    content = {
        'data_set': MC.objects.filter(**kwargs),
            }
    return render_to_response('mc.html', RequestContext(request, content))


def filter_flower(request, category):
    subclass = None
    if category == 'door':
        subclass = C_FLOWER_STYLE_DOOR
    elif category == 'road':
        subclass = C_FLOWER_STYLE_ROAD
    elif category == 'desk':
        subclass = C_FLOWER_STYLE_DESK

    kwargs = dict()
    content = {
        'subclass': subclass,
        'data_set': S_Flower.objects.filter(**kwargs),
        }
    return render_to_response('flower.html', RequestContext(request, content))
