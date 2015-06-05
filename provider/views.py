#-*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

import base.choices as choice_set
from provider.models import ProviderInfo


t_dict = {k: v for k, v in choice_set.C_PRODUCT_TYPE}


def provider(request, c_type):
    data = ProviderInfo.objects.filter(type=c_type)

    content = {
        'data_set': data,
        'c_type': c_type,
        'disp_name': t_dict[c_type],
        }
    return render_to_response('provider.html', RequestContext(request, content))
