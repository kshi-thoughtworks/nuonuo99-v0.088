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


type_map = {
    'mc': MC,
    'makeup': MakeUp,
    }


def filter_html(request):
    type_key = request.GET.get('type', '').lower()

    type_model = type_map.get(type_key, None)
    if type_model is None:
        return render_to_response('50x.html', RequestContext(request))

    kwargs = expert_filter(request.GET)
    content = {
        'data_set': type_model.objects.filter(**kwargs),
            }
    return render_to_response('%s.html' % type_key, RequestContext(request, content))
