#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

import django_filters

import std_product.models
import std_product.filters

import base.choices as choice_set


def product_home(request, type, cate):
    model = getattr(std_product.models, type)
    filter = getattr(std_product.filters, '%s_filter' % type)
    paras = getattr(choice_set, '%s_paras' % type)
    choice = getattr(choice_set, 'get_disp_%s_cate' % type)

    data = filter(request.GET, queryset=model.objects.filter(category=cate))

    content = {
        'paras': paras(cate),
        'cart_url': 'add_product_%s' % type,
        'data_set': data,
        'type': type,
        'cate': cate,
        'disp_name': choice(cate),

        'flower_cate': choice_set.C_FLOWER_CATE,
        'av_cate': choice_set.C_AV_CATE,
        'stage_cate': choice_set.C_STAGE_CATE,
        }
    return render_to_response('std_product.html', RequestContext(request, content))
