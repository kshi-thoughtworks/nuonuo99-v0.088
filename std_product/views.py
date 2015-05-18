#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from std_product.models import WedFlower

from base.choices import C_FLOWER_STYLE_DOOR,C_FLOWER_STYLE_OTHERS

from base.models import C_FlowerStyle

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
    f_style = C_FlowerStyle.objects.filter(category=cate)

    kwargs = price_filter(request.GET)
    content = {
        'f_style': f_style,
        'cart_url': 'add_product_flower',
        'data_set': WedFlower.objects.filter(**kwargs),
        }
    return render_to_response('flower.html', RequestContext(request, content))
