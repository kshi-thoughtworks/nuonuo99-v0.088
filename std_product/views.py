#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from std_product.models import WedFlower

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def price_filter(query_set):
    kwargs = dict()
    bottom, top = query_set.get('price', '-').split('-')

    if bottom:
        kwargs['price__gte'] = bottom

    if top:
        kwargs['price__lte'] = top

    return kwargs


def filter_flower(request, cate):
    kwargs = price_filter(request.GET)

    query_set = request.GET

    def add_para(db, para):
        value = query_set.get(para, '0')
        if value != '0':
            kwargs[db] = value

    add_para("style", "f_style")

    content = {
        'f_style': [],
        'cart_url': 'add_product_flower',
        'data_set': WedFlower.objects.filter(category=cate, **kwargs),
        }
    return render_to_response('flower.html', RequestContext(request, content))
