#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from std_product.models import WedFlower

from base.choices import C_FLOWER_STYLE_DOOR,C_FLOWER_STYLE_OTHERS

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def price_filter(query_set):
    kwargs = dict()
    bottom, top = query_set.get('price', '-').split('-')

    if bottom:
        kwargs['price__gte'] = bottom

    if top:
        kwargs['price__lte'] = top

    return kwargs


type_map = {
    'flower': WedFlower,
    }


category_map = {
    'door': C_FLOWER_STYLE_DOOR.CHOICES,
    'road': C_FLOWER_STYLE_OTHERS.CHOICES,
    'desk': C_FLOWER_STYLE_OTHERS.CHOICES,
    }


def filter_html(request, type_key):
    type_model = type_map.get(type_key, None)
    if type_model is None:
        return render_to_response('404.html', RequestContext(request))

    cate_key = request.GET.get('cate', '').lower()
    category = category_map.get(cate_key, None)

    kwargs = price_filter(request.GET)
    content = {
        'category': category,
        'data_set': type_model.objects.filter(**kwargs),
        }
    return render_to_response('%s.html' % type_key, RequestContext(request, content))
